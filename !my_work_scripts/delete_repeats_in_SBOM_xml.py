import xml.etree.ElementTree as ElementTree
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--SbomFile')
parser.add_argument('--OutputFile', nargs='?')
args = parser.parse_args()

ElementTree.register_namespace('', "http://cyclonedx.org/schema/bom/1.3")

tree = ElementTree.parse(args.SbomFile)
root = tree.getroot()

output_json = {}
unique_components = []
unique_dependencies = []

# убрать повторения в списке component
for component in root[1]:
    try:
        if component.attrib['bom-ref'] not in unique_components:
            unique_components.append(component.attrib['bom-ref'])
        else:
            root[1].remove(component)
    except KeyError:
        continue

#убрать повторения в списке dependencies
for dependency in root[2]:
    if dependency.attrib['ref'] not in unique_dependencies:
        unique_dependencies.append(dependency.attrib['ref'])
    else:
        root[2].remove(dependency)

tree.write(args.SbomFile)

if args.OutputFile:
    for unique_component in unique_components:
        if "pkg:nuget" in unique_component:
            packageName = unique_component.split('@', 1)[0].split('pkg:nuget/', 1)[1]
            version = unique_component.split('@', 1)[1]
            # print(packageName, version)
            output_json[packageName] = version
    with open(args.OutputFile, 'w', encoding='utf-8') as f:
        json.dump(output_json, f, ensure_ascii=False, indent=4)