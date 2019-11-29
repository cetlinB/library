from flask import Flask
from pymongo_helplib import MongoClient

app = Flask(__name__)

db = MongoClient("mongodb+srv://ctcluster-ph4yr.mongodb.net/CTDatabase",
                 username='CTDatabaseUser',
                 password='plan-b-po'
                 )

@app.route('/library/launcher/applications')
def get_applications():
    return "Ok",200

@app.route('/library/launcher/applications/<int:id>')
def get_application(id):
    return "OK", 200

