import requests
import json

from id import *

class SpotifyAuth:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def server_auth(self, country='US', limit=10):
        res = {}
        token_url = 'https://accounts.spotify.com/api/token'
        new_rel_url = f'https://api.spotify.com/v1/browse/new-releases?country={country}&limit={limit}'

        data = {'grant_type': 'client_credentials'}
        token_response = requests.post(token_url, data=data, \
            verify=True, allow_redirects=False, \
            auth=(client_id, client_secret))

        tokens = json.loads(token_response.text)

        access_token = tokens['access_token']

        api_headers = {'Authorization': f'Bearer {access_token}'}
        api_response = requests.get(new_rel_url, headers=api_headers, verify=True)

        res = api_response.json()
        return res

class FilterRelease(SpotifyAuth):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id, client_secret)
    
    def filtered(self):
        import random
        import itertools
        ri = random.randint(0,9)
        release_results = super().server_auth(country='US', limit=10)
        artists = release_results['albums']['items'][ri]['artists']
        
        artist_list = []
        for d in artists:
            for v,l in d.items():
                artist_list.append(l)

        f_artist = artist_list[3]
        name = release_results['albums']['items'][ri]['name']
        release_date = release_results['albums']['items'][ri]['release_date']
        uri = release_results['albums']['items'][ri]['uri']
        
        return {
            "Artist": f_artist,
            "name": name,
            "release date": release_date,
            "Spotify URI": uri
        }
