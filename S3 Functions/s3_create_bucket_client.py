import boto3
def s3_create_bucket_client(bucket_name):
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    return response

s3_create_bucket_client('rsk-qa')