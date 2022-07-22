
import json
from config import Config
import boto3
from botocore.client import Config as BootConfig
from botocore.exceptions import ClientError
from boto3.session import Session
from models.account_info import accountInfo
from models.video_information import videoInformation
import uuid
from bson import json_util, ObjectId

class videos:

    def __init__(self):
        pass

    def get_files(self, params):

        query = {
            "account_id" : params['account_id']
        }

        response = videoInformation.objects(**query)
        res = []
        for each_record in response:
            temp = each_record._data
            del temp['id']
            res.append(temp)
        return json.dumps(res)

videos_details = videos()