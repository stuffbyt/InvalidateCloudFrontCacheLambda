# InvalidateCloudFrontCacheLambda
Use this easy to understand boto3 script to invalidate CloudFront cache every time there is a new version of your file in s3 bucket

# Services used

CloudFront - S3 - Lambda 

Lambda has a trigger added to it so that when you upload a new file to the s3 bucket, it will invoke the Lambda function, which will then extract the file name to be invalidated from the given CloudFront distribution. 
