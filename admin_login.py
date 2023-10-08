#to receive username and password #class can be used to reusability of sql
from flask import Blueprint,request
from classModules.userClass import objUsers
import hashlib  #built in module available in python

users_blueprint=Blueprint('users_blueprint',__name__)
@users_blueprint.route('/validate-cred',methods=['POST'])    #@ is in decorator in python
def chkAdminUser():
    username= request.form['username']
    password=request.form['password']

    if not username and not password:
        return '[{"errMsg":1,"message":"Invalid Credentials"}]'#return in json data or by yourself is called json serialization
    
    #Encrypt password to SHA256
    encPassword=hashlib.sha256(password.encode('utf-8')).hexdigest()

    resultValue=objUsers.validateCred(username,encPassword)
     
    if resultValue==0:
        return '[{"errFlag":1,"message":"Invalid Credentials"}]'
    else:
        return resultValue  #upto this the first API