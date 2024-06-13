import boto3
def create_s3_bucket_recurso(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.create()
    return bucket

create_s3_bucket_recurso('rsk-dev')