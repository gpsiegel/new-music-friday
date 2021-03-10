import requests
import base64
import json

from id import *

country = 'US'
limit = 10

token_url = 'https://accounts.spotify.com/api/token'

new_rel_url = f'https://api.spotify.com/v1/browse/new-releases?country={country}&limit={limit}'

data = {'grant_type': 'client_credentials'}


token_response = requests.post(token_url, data=data, \
    verify=True, allow_redirects=False, \
    auth=(client_id, client_secret))

print(token_response.headers)
print(token_response.text)

tokens = json.loads(token_response.text)

access_token = tokens['access_token']

api_headers = {'Authorization': f'Bearer {access_token}'}
api_response = requests.get(new_rel_url, headers=api_headers, verify=True)

print(api_response.text)
