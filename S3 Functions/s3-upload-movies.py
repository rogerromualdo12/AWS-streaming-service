import boto3

def upload_movies_s3(bucketName,uploadFile):
    s3 = boto3.resource('s3')
    bucket = s3.Object(bucketName,uploadFile)
    bucket.upload_file(uploadFile)
    return bucket

upload_movies_s3('rsk-dev','datosPeliculas.json')