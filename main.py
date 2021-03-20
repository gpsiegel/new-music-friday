import requests
import json
import boto3
import uuid

from id import *
from api import FilterRelease

def main():
    #Instantiating the Spotify API
    api_client = FilterRelease(client_id, client_secret)

    #Beginning to sort the results
    post = []
    sorting = api_client.filtered()

    for s in sorting.values():
        post.append(s)

    #sorted values
    artist = post[0]
    name = post[1]
    release_date = post[2]
    uri = post[3]

    #ddb insert
    ddb = boto3.resource('dynamodb', \
        aws_access_key_id=AWS_KEY, \
        aws_secret_access_key=AWS_SECRET_KEY, \
        region_name="us-east-1")
    table = ddb.Table('NRF')
    id = str(uuid.uuid4())

    new_release = table.put_item(Item={
        "id":  id,
        "Artist": artist,
        "Name": name,
        "Release_Date": release_date,
        "Spotify_URI": uri
    })

    return new_release

if __name__ == "__main__":
    main()
