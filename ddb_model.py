import boto3 
import uuid

class DDBModel:

    def new_record(self, artist, name, release_date, uri):
        ddb = boto3.resource('dynamodb')
        table = ddb.Table('NRF')
        id = uuid.uuid4()

        new_release = {
            'id': id,
            'Artist': artist,
            'Name': name,
            'Release_Date': release_date,
            'Spotify_URI': uri
        }

        table.put_item(Item=new_release)
