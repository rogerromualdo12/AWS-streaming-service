import boto3
print('Lista de buckets mediante resource: ')
s3resource = boto3.resource('s3','us-east-1')
buckets = s3resource.buckets.all()
for bucket in buckets:
    print(f'\t{bucket.name}') 

print('Lista de buckets mediante cliente: ')
s3client = boto3.client('s3')
response = s3client.list_buckets()
for bucket in response['Buckets']:
    print(f'\t{bucket["Name"]}')