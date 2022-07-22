
from flask import Flask, jsonify, request, render_template, Response
from services.file_upload import upload_to_s3
from services.register import registration
from services.login import login_i
from services.videos import videos_details
from flask_mongoengine import MongoEngine
from config import Config
import json

db = MongoEngine()

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
  
@app.route('/upload')
def home():
    return render_template('file_upload_form.html')
  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        content_type = request.mimetype 
        print(upload_to_s3.upload_to_s3(file_data=f, file_name=f.filename, content_type=content_type, payload=request))
        return render_template("success.html", name = f.filename) 

@app.route('/register_page')  
def register_page():  
    return render_template('register.html')

@app.route('/login_page')  
def login_page():  
    return render_template('login.html')    

@app.route('/registration', methods = ['POST'])  
def register():  
    if request.method == 'POST':  
        response = registration.register(request)
        return render_template('login.html', msg=response['message']) 

@app.route('/get_video_files', methods = ['GET'])  
def videos():
    query_params = request.args.to_dict(flat=True) 
    response = videos_details.get_files(query_params)
    return Response(response, mimetype='application/json')

@app.route('/dashbord')  
def dashbord():
    query_params = request.args.to_dict(flat=True) 
    response = videos_details.get_files(query_params)
    return render_template('dashbord.html', records = json.loads(response)) 

@app.route('/login', methods = ['POST'])  
def login():  
    if request.method == 'POST':  
        response = login_i.login_method(request)
        if response['status']:
            return render_template('dashbord.html', msg=response['message'], account_id=response['account_id']) 
        else:
            return render_template('login.html', msg=response['message']) 


if __name__ == '__main__':
    app.run(debug = True)