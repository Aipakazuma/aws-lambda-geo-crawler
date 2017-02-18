# -*- coding:utf-8 -*-
# lambda_function.py
import boto3

AWS_S3_BUCKET_NAME = 'geo.list.html'

def lambda_handler(event, context):
  s3_client = boto3.resource('s3')
  bucket = s3_client.Bucket(AWS_S3_BUCKET_NAME)
  print bucket.name

  # list
  # 階層を作ると、一番最下層までファイルを読み出してくれる
  for object in bucket.objects.all():
    print object.key

  # upload
  # bucket.upload_file('./event.json', 'event.json')
  # ディレクトリを追記したら、一緒に追加された
  bucket.upload_file('./event.json', 'test/event.json')
  # 存在するディレクトリを追記したままでも上書きされず、ファイルだけが追加される
  bucket.upload_file('./event.json', 'test/event2.json')
  bucket.upload_file('./event.json', 'test/test2/event.json')

  # download
  # bucket.download_file('event.json', 'event2.json')

  # delete
  # 階層が存在しても削除することができる
  for object in bucket.objects.all():
    object.delete()

  return
