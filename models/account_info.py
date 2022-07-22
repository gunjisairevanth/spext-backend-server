from email.policy import default
from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField



class accountInfo(DynamicDocument):


    _id = StringField()

    account_id = StringField()

    email = StringField()

    password = StringField()

    auth_token = StringField(default="")

    meta = {
        "collection": "account_info",
        }