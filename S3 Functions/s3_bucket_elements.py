import boto3
def S3_bucket_elements(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    for object in bucket.objects.all():
        print(object.key)
    return bucket

S3_bucket_elements('rsk-dev')