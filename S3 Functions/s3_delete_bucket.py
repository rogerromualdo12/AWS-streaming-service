import boto3
def s3_delete_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)    
    bucket.objects.delete()
    bucket.delete()
    return bucket

s3_delete_bucket('rsk-test')