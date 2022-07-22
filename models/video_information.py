from mongoengine import DynamicDocument, IntField, StringField, DateTimeField, DictField, FloatField



class videoInformation(DynamicDocument):
    


    # _id = StringField()

    account_id = StringField()

    video_id = StringField()

    video_title = StringField()

    is_public = IntField(default=0)

    public_url = StringField(default="")

    like = IntField(default=0)

    dislike = IntField(default=0)

    views = IntField(default=0)

    duration = IntField(default=0)

    transcode_status = IntField(default=0)

    s3_file_path = StringField(default="")


    meta = {
        "collection": "video_information",
        }