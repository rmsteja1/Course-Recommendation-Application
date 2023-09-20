from flask import Flask, request
from flask_mail import Mail
from flask_cors import CORS
#from flask_pymongo import PyMongo
import pymongo
app=Flask(__name__)
# app.config["SECRET_KEY"]= "f42d1da22cfd4e18f6a1177e5989c3bcb99af25"
CORS(app, support_credentials=True)
# mongodb connection
app.config["MONGO_URI"] = "mongodb+srv://cmpe295bavengers:G9p8xQP6DWHZxdP6@cluster0.jn5gbkj.mongodb.net/?retryWrites=true&w=majority"
conn = "mongodb+srv://cmpe295bavengers:G9p8xQP6DWHZxdP6@cluster0.jn5gbkj.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn, serverSelectionTimeoutMS=5000)
db = client.db

# mail sending configuration
app.config['MAIL_SERVER']='smtp.mailgun.org'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'postmaster@sandbox432c581edfb24033a9fd16bfaa224f08.mailgun.org'
app.config['MAIL_PASSWORD'] = '6e5687ddc0dcbe93e2b2a5528d87b198-181449aa-9afcbfb3'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['SECRET_KEY'] = 'finalproject'
mail = Mail(app)




from application import recommendationroutes
from application import routes


