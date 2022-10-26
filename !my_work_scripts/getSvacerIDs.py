import argparse
import requests
from requests.auth import HTTPBasicAuth
import json
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('--SvacerUser')
parser.add_argument('--SvacerPassword')
parser.add_argument('--SvacerProject')
parser.add_argument('--branch', default='master')
parser.add_argument('--snapshot')
parser.add_argument('--SvacerUrl', nargs='?', default='http://vmsvacer.aladdin.ru/')
args = parser.parse_args()

idProject = ''
idBranch = ''
idShapshot = ''
output_json = {}
output_file = 'SvacerIDs.json'

if os.path.exists(output_file):
    os.remove(output_file)

auth = HTTPBasicAuth(args.SvacerUser, args.SvacerPassword)
resp = requests.post(url='http://vmsvacer.aladdin.ru/api/login?auth_type=ldap&server=ALADDIN.RU', auth=auth)
# resp.status_code

auth_contents = resp.json()
svacerToken = auth_contents['token']
# print (auth_contents)

if not svacerToken:
    print('Authentication failed! Please enter valid svacer credentials!')
    sys.exit()
# else:
#     print (svacerToken)
output_json['svacerToken'] = svacerToken

response = requests.get(url=args.SvacerUrl + 'api/public/projects', headers={'Authorization': 'Bearer ' + svacerToken})
projects_contents = response.json()
# print (projects_contents)
print(response)
if not projects_contents:
    print('Fail to get svacer projects data!')
    sys.exit()

for project in projects_contents:
    if project['project']['name'] == args.SvacerProject:
        idProject = project['project']['id']
        branches = project['branches']
        for branch in branches:
            if branch['name'] == args.branch:
                idBranch = branch['id']

if not idProject or not idBranch:
    print('Can not get Project ID or Branch ID!')
    sys.exit()

output_json['idProject'] = idProject
output_json['idBranch'] = idBranch

response_snapshots = requests.get(
    url=args.SvacerUrl + 'api/public/projects/' + idProject + '/branch/' + idBranch + '/snapshots',
    headers={'Authorization': 'Bearer ' + svacerToken})
print(response_snapshots)
snapshots_contents = response_snapshots.json()
# print(snapshots_contents)

if not snapshots_contents:
    print('Fail to get svacer snapshot contents!')
    sys.exit()

for snapshot in snapshots_contents:
    if snapshot['name'] == args.snapshot:
        idShapshot = snapshot['id']

if not idShapshot:
    print('Fail to get snapshot ID!')
    sys.exit()

output_json['idShapshot'] = idShapshot

# print(output_json)
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_json, f, ensure_ascii=False, indent=4)