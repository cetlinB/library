from flask import Flask, request
from pymongo_helplib import MongoClient
from application.database import DBProvider

app = Flask(__name__)

db = MongoClient("mongodb+srv://ctcluster-ph4yr.mongodb.net/CTDatabase",
                 username='CTDatabaseUser',
                 password='plan-b-po'
                 )

db_worker = DBProvider()

@app.route('/library/launcher/applications')
def get_applications():
    if request.method == 'GET':
        return db_worker.getApplications()
    elif request.method == 'POST':
        db_worker.saveApplicationFromForm(request.form)
        return "OK", 200
    return "Not implemented", 501

@app.route('/library/launcher/applications/<int:id>')
def get_application(id):
    return "OK", 200

