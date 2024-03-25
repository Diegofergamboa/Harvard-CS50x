import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()


response = requests.get(f'https://itunes.apple.com/search?entity=song&limit=20&term={sys.argv[1]}')
data = response.json()

for result in data['results']:
    print(result["trackName"])