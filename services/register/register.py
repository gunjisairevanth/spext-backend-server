from config import Config
import cryptocode
import uuid
from models.account_info import accountInfo

class register():
    def __init__(self):
        pass

    def register(self,request):
   
        # encoded = cryptocode.encrypt(Config.SALT,request.form['password'])
        # decoded = cryptocode.decrypt(encoded, request.form['password'])

        password = request.form['password']
        repassword = request.form['repassword']

        if repassword!=password:
            return {
                "status" : False,
                "message" : "<p>password not mached</p>"
            }
        else:
            try:
                password = cryptocode.encrypt(Config.SALT,request.form['password'])
                payload = {
                    "account_id" : str(uuid.uuid4()),
                    "email" : request.form['email'],
                    "password" : password
                }
                query = {
                    "email" : request.form['email']
                }
                response = accountInfo.objects(**query)
                if len(response)==0:
                    accountInfo(**payload).save()
                    return {
                        "status" : True,
                        "message" : "<p>Registred Sucessfully</p>"
                    }
                else:
                    return {
                        "status" : True,
                        "message" : "<p>User Already Exist</p>"
                    }
            except:
                return {
                    "status" : False,
                    "message" : "<p>User Already Exist</p>"
                }
    
        return payload

registration = register()