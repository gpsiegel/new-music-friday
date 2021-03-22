import json
import os
import logging
import datetime
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')
SNS_TOPIC = os.environ['SNS_TOPIC']
today = datetime.date.today()


def lambda_handler(event, context):
    resp = {'Items': []}

    if not 'Records' in event:
        resp = {"error_message" : 'No Records found' }
        return resp
    
    logger.debug(f"Event:{event}")
    for r in event.get('Records'):
        if r.get('eventName') == "INSERT":
            d = {}
            d['Artist'] = r['dynamodb']['NewImage']['Artist']['S']
            d['Name'] = r['dynamodb']['NewImage']['Name']['S']
            d['Release_Date'] = r['dynamodb']['NewImage']['Release_Date']['S']
            d['Spotify_URL'] = r['dynamodb']['NewImage']['Spotify_URL']['S']

            resp['Items'].append(d)
    
    process = []
    for more in resp['Items']:
        for k,v in more.items():
            process.append(v)
    
    artist = process[0]
    name = process[1]
    date = process[2]
    url = process[3]
    
    subject = f"New Music Fridays - {today}"
    message = f"{artist} just released {name} on {date}! Check it out at {url}"
    
    pub = sns.publish(
        TopicArn=SNS_TOPIC,
        Message=message,
        Subject=subject
        )

    logger.info(f"resp:{pub}")
    return pub
