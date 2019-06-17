# When you upload an object to your s3 bucket, this Lambda function will be invoked. The function pretty much extracts the 
# keyname and makes a invalidate cache API call against CloudFront. You also need a caller reference when making API call 
# against CloudFront and for that we're using timestamp. 


import json
import boto3
client = boto3.client('cloudfront') #CFClient for boto 
import time
import urllib
from pprint import pprint


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event)) #Lambda event handler for boto3 + Print events on CW logs 
    objectname = event['Records'][0]['s3']['object']['key'] #extracts the keyname/path name from the s3 event log
    ObjectListToInvalidate= []
    ObjectListToInvalidate.append(objectname)
    timestring = str(time.time())
    timestringSecond = (timestring.split("."))
    print (timestringSecond [0])
    mystr1 = "/"+ ObjectListToInvalidate[0]
    response = client.create_invalidation(
    DistributionId='E1OAHO3XQ1HAUL',  #update this with your distribution ID
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
