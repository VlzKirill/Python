import xml.etree.ElementTree as ElementTree
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--NugetMD5')
parser.add_argument('--NugetComponentName')
parser.add_argument('--AllMD5File')
parser.add_argument('--SBOM', default='SBOM_all.xml')
args = parser.parse_args()

ElementTree.register_namespace('', "http://cyclonedx.org/schema/bom/1.3")
tree = ElementTree.parse(args.SBOM)
root = tree.getroot()


def compare_lines_in_files(file1, file2):
    with open(file1) as f1:
        f1lines = f1.readlines()
        for f1line in f1lines:
            f1line = f1line.strip()
            if f1line == '':
                continue
            with open(file2) as f2:
                f2file = f2.read()
                if f1line in f2file:
                    return True
                    break


if not bool(compare_lines_in_files(args.NugetMD5, args.AllMD5File)):
    print(f"Компонента {args.NugetComponentName} нет в проекте!")
    for component in root[1]:
        try:
            packageName = component.attrib['bom-ref'].split('@', 1)[0].split('pkg:nuget/', 1)[1]
            if packageName == args.NugetComponentName:
                root[1].remove(component)
                print(f"Компонент {args.NugetComponentName} удален из SBOM!")
                break
        except KeyError:
            continue
    for dependency in root[2]:
        packageName = dependency.attrib['ref'].split('@', 1)[0].split('pkg:nuget/', 1)[1]
        if packageName == args.NugetComponentName:
            root[2].remove(dependency)
            print(f"Зависимости компонента {args.NugetComponentName} удалены из SBOM!")
            break
    tree.write(args.SBOM)