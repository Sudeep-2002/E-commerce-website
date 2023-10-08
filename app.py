#.venv comes with flask in that virtual environment on that create environment on that windows last line copy and paste that in run to obtained in cmd
#in the next we use activate the environment in copy the windows of .venv\Sripts\activate in paste to cmd
#we install flsk paste it in the cmd pip install flask
#python --version to put in cmd to get version of python
#app.py to link admin_login file
from flask import Flask
from flask_cors import CORS
from db import db
from admin_login import users_blueprint
from home import product_blueprint
from admin_dashboard import admin_dashboard_blueprint

app=Flask(__name__)
CORS(app)
#DB Config
username='root'
password=''#Admin_123
server='127.0.0.1'
dbname='/ecommerce_store'
userpass='mysql+pymysql://'+username+':'+password+'@'

app.config['SQLALCHEMY_DATABASE_URI']=userpass+server+dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app) #setting the values in sql alchamey
#register blueprint
app.register_blueprint(users_blueprint) #users_blueprint is a function to connect or link to userClass.py
app.register_blueprint(product_blueprint)
app.register_blueprint(admin_dashboard_blueprint)



@app.route('/server')
def serverStatus():
    return "Server is up and running"
#sum of two numbers      #we can give url 127.0.0.1:8080/sum 
@app.route('/sum')
def sumTwoNumbers():
    a=10
    b=30
    return str(a+b)
#power exponential problem  #we can give url 127.0.0.1:8080/power/exponential
@app.route('/power/exponential')
def power1():
    a=10
    b=3
    return str(a**b)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)      #https://api.postalpincode.in/pincode/572201 to give in browser to give tiptur pincode villages
    #ctrl C stop the server