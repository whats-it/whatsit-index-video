import json

import boto3
import dropbox
import requests

from . import Config

AWS_ACCESS_KEY = Config.getValue('AWS', 'AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = Config.getValue('AWS', 'AWS_SECRET_ACCESS_KEY')


def download_file(save_path, file_url):
    """ Download file from http url link """

    r = requests.get(file_url)  # create HTTP response object

    with open(save_path, 'wb') as f:
        f.write(r.content)

    return save_path


def download_file_from_dropbox(save_path, link):
    """ Download file from dropbox
    It is need to get a app access token"""

    dbx = dropbox.Dropbox("Access Token")
    print(dbx.users_get_current_account())

    return dbx.sharing_get_shared_link_file(url=link, path=save_path)


def upload_file_to_bucket(bucket, file_path, key):
    """ Upload files to S3 Bucket """
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    with open(file_path, 'rb') as data:
        s3.upload_fileobj(data, bucket, key)


def request_service(url, params):
    resp = requests.get(url=url, params=params)
    return json.loads(resp.text)
