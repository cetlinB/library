from flask import request
from application.database import DBProvider
from application import app
import json

db_worker = DBProvider()

db_worker.getApplicationsDictionaty()


@app.route('/library/launcher/applications')
def get_applications():
    if request.method == 'GET':
        return json.dumps(db_worker.getApplicationsDictionaty())
    elif request.method == 'POST':
        db_worker.saveApplicationDictionary(request.form)
        return "OK", 200
    return "Not implemented", 501


@app.route('/library/launcher/applications/<int:id>')
def get_application(id):
    return "OK", 200
