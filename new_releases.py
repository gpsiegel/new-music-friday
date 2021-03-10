import requests
import base64
import json

import id

class NewReleaseAPI(object):
    
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
    
    def auth(self):
        token_url = 'https://accounts.spotify.com/api/token'
        headers = {}
        data = {}

        payload = f"{client_id}:{client_secret}"
        payload_ascii = payload.encode('ascii')
        base64_byte = base64.b64encode(payload_ascii)
        base64_payload = base64_byte.decode('ascii')

        headers['Authorization'] = f"Basic {base64_payload}"
        data['grant_type'] = "client_credentials"

        req = requests.post(token_url, headers=headers, data=data)
        token = req.json()['access_token']
    
    def releases(self, country=US, limit=10):
        auth = self.auth()
        new_rel_url = f'https://api.spotify.com/v1/browse/new-releases?country={country}&limit={limit}'
        headers = {
            "Authorization": "Bearer " + auth.token
        }
        results = requests.get(url=new_rel_url, headers=headers)

        print(json.dumps(results.json()))
