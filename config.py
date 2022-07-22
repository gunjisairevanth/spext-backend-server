from os import getenv, path
from dotenv import load_dotenv

APP_ROOT = path.join(path.dirname(__file__), '.')   # refers to application_top
dotenv_path = path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


class Config(object):

    S3_BUCKET = getenv('S3_BUCKET','test')
    AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID','test')
    AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY','test')
    AWS_REGION = getenv('AWS_REGION','test')
    SALT = getenv('SALT','test')
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY','test')

    MONGODB_SETTINGS =  {
    'db': getenv('MONGO_DATABASE'),
     #getenv('MONGODB_URI')
    #'host':getenv('MONGODB_URI'),
    'host': "mongodb+srv://{}:{}@{}/{}".format(getenv('MONGO_USER'),getenv('MONGO_PASSWORD'),getenv('MONGO_HOST'),getenv('MONGO_DATABASE'))
    }
