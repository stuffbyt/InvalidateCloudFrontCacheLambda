import json
import boto3
client = boto3.client('cloudfront')
import time
import urllib
from pprint import pprint


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    objectname = event['Records'][0]['s3']['object']['key']
    ObjectListToInvalidate= []
    ObjectListToInvalidate.append(objectname)
    timestring = str(time.time())
    timestringSecond = (timestring.split("."))
    print (timestringSecond [0])
    mystr1 = "/"+ ObjectListToInvalidate[0]
    response = client.create_invalidation(
    DistributionId='E1OAHO3XQ1HAUL',
    InvalidationBatch={
        'Paths': {
            'Quantity': 1,
            'Items': [
                mystr1,
            ]
        },
        'CallerReference': timestringSecond [0]
    }
)
