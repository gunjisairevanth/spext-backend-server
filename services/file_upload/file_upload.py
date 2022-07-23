
from config import Config
import boto3
from botocore.client import Config as BootConfig
from botocore.exceptions import ClientError
from boto3.session import Session
from models.account_info import accountInfo
from models.video_information import videoInformation
import uuid

class fileUpload:

    def __init__(self):
        pass

    def _s3_resource(self):

        self._s3 = boto3.Session(
            aws_access_key_id= Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=  Config.AWS_SECRET_ACCESS_KEY,
            region_name = Config.AWS_REGION
            )

    def create_record(self, payload, file_path):

        payload = {
                "account_id" : payload.form['account_id'],
                "video_title": payload.form['title'],
                "video_id" : str(uuid.uuid4()),
                "is_public" : (1 if payload.form['public_access'] == 'yes' else 0),
                "public_url" : str(uuid.uuid4()),
                "transcode_status" : 0,
                "s3_file_path" : file_path,
        }
        videoInformation(**payload).save()

    def upload_to_s3(self, file_data, file_name, content_type, payload):

        self._s3_resource()

        file_path = 'user_uploads/{}/{}'.format(str(uuid.uuid4()),file_name)

        self._s3.client('s3').put_object(Bucket=Config.S3_BUCKET, Key=file_path, Body=file_data,  ContentType='video/mp4')
        
        self.create_record(payload,file_path)

        return Config.S3_BUCKET



upload_to_s3 = fileUpload()