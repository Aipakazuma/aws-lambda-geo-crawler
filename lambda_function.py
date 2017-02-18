# lambda_function.py
import boto3

AWS_S3_BUCKET_NAME = 'geo.list.html'

def lambda_handler(event, context):
  s3_client = boto3.resource('s3')
  bucket = s3_client.Bucket(AWS_S3_BUCKET_NAME)
  print bucket.name

  # list
  for object in bucket.objects.all():
    print object.key

  # upload
  bucket.upload_file('./event.json', 'event.json')

  # download
  bucket.download_file('event.json', 'event2.json')

  # delete
  for object in bucket.objects.all():
    object.delete()


  return
