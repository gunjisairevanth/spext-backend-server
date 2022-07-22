
from config import Config
import cryptocode
from models.account_info import accountInfo
import datetime
import jwt

class login():
    def __init__(self):
        pass

    def login_method(self,request):

        query = {
            "email" : request.form['email']
        }
        response = accountInfo.objects(**query)

        print("response ----> ",response)
        if len(response)!=0:

            encoded = response[0]['password']
            decode = cryptocode.decrypt(encoded, request.form['password'])

            if decode == Config.SALT:

                json_data = {
                    "payload": {
                        "account_id" : response[0]['account_id'],
                        "email" : response[0]['email']
                    },
                    "date": str(datetime.datetime.now())
                }

                encode_data = jwt.encode(payload=json_data, \
                        key=Config.JWT_SECRET_KEY, algorithm="HS256")

                payload ={"auth_token" : str(encode_data)}


                accountInfo.objects(**query).update(**payload)

                return {
                    "status" : True,
                    "message" : encode_data,
                    "account_id" : response[0]['account_id']
                }

            else:

                return {
                    "status" : False,
                    "message" : "Invalid Password"
                }
        else:
            return {
                "status" : False,
                "message" : "Email not exist"
            }

login_i = login()