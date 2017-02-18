# -*- coding:utf-8 -*-
# lambda_function.py
import boto3
from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import URLError
from urllib2 import HTTPError

AWS_S3_BUCKET_NAME = 'geo.list.html'


def get_web_resource(url):
  try:
    return urlopen(url)
  except HTTPError as e:
    print e
  except URLError as e:
    print 'The server could not be found!'
  return None


def lambda_handler(event, context):
  s3_client = boto3.resource('s3')
  bucket = s3_client.Bucket(AWS_S3_BUCKET_NAME)
  print bucket.name

  # url = 'http://www.yahoo.co.jp'
  # resource = get_web_resource(url)
  # html_resource = resource.read()

  # upload
  # bucket.put_object(Key='test/www.yahoo.co.jp.html', Body=html_resource)

  for object in bucket.objects.all():
    html_object = object.get()['Body'].read()
    print html_object.decode('utf-8')

  return
