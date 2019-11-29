from flask import request, render_template
from application.database import DBProvider
from application import app
import json

db_worker = DBProvider()

db_worker.getApplicationsDictionaty()

dummySchema = [
                        {
                            "name": "Variable X",
                            "type": "int",
                            "defaultValue": 1
                        },

                        {
                            "name": "Variable Y",
                            "type": "int",
                            "defaultValue": 2
                        },

                        {
                            "name": "Variable Z",
                            "type": "int",
                            "defaultValue": 3
                        }
    ]

@app.route('/library/launcher/applications', methods={'POST','GET'})
def get_applications():
    if request.method == 'GET':
        return json.dumps(db_worker.getApplicationsDictionaty())
    elif request.method == 'POST':
        form_data = request.form
        app = {
            'id':db_worker.getApplicationsDictionaty().__len__(),
            'name':form_data['name'],
            'description':form_data['description'],
            'icon':form_data['icon'],
            'schema': dummySchema
        }
        db_worker.saveApplicationDictionary(app)
        return "OK", 200
    return "Not implemented", 501


@app.route('/library')
def application_add_form():
    if request.method == 'GET':
        return render_template('app_form.html')

@app.route('/library/launcher/applications/<int:id>')
def get_application(id):
    return "OK", 200
