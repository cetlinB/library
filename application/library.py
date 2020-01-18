from flask import request, render_template
from application.database import DBProvider
from application import app
import json

db_worker = DBProvider()

dummySchema = [
                        {
                            "name": "N",
                            "type": "int",
                            "defaultValue": "10"
                        }
    ]

schemaMoreDummyThanDummy = [

]

otherSchema = [
                        {
                            "name": "Variable X",
                            "type": "int",
                            "defaultValue": "1"
                        },
                        {
                            "name": "Variable Y",
                            "type": "int",
                            "defaultValue": "2"
                        },
                        {
                            "name": "Variable Z",
                            "type": "int",
                            "defaultValue": "3"
                        }
]

computation_step_package_fibonacci = {
        "applicationId": "",
        "computationSteps":[
            {
                "artifactUrl": "fib_list:latest",
                "command": "",
                "params": [
                    {
                        "name": "N",
                        "type": "int",
                        "defaultValue": 10
                    }
                ]
            },
            {
                "params": [],
                "artifactUrl": "fib_sum:latest",
                "command": ""
            }
        ],
        "version":"0.01.1"
    }

computation_step_package_cyberpunk = {
        "applicationId": "",
        "computationSteps":[
            {
                "artifactUrl": "cyberpunk2077.exe",
                "command": "Run Cyberpunk2077",
                "params": []
            }
        ],
        "version":"2020.09.17"
    }

computation_step_package_default = {
        "applicationId": "",
        "computationSteps":[
            {
                "artifactUrl": "default",
                "command": "default",
                "params": [
                        {
                            "name": "Variable X",
                            "type": "int",
                            "defaultValue": "1"
                        }
                ]
            },
            {
                "artifactUrl": "default",
                "command": "default",
                "params": [
                        {
                            "name": "Variable Y",
                            "type": "int",
                            "defaultValue": "2"
                        }
                ]
            },
            {
                "artifactUrl": "default",
                "command": "default",
                "params": [
                        {
                            "name": "Variable Z",
                            "type": "int",
                            "defaultValue": "3"
                        }
                ]
            }
        ],
        "version":"2020.07.07"
    }

@app.route('/library/launcher/applications', methods={'POST','GET'})
def get_applications():
    if request.method == 'GET':
        return json.dumps(db_worker.getApplicationsDictionary())
    elif request.method == 'POST':
        form_data = request.form
        print(dummySchema if 'fibonacci' in form_data else (schemaMoreDummyThanDummy if 'nothing' in form_data else otherSchema))
        app = {
            'id': db_worker.getApplicationsDictionary().__len__(),
            'name': form_data['name'],
            'description': form_data['description'],
            'icon': form_data['icon'],
            'schema': dummySchema if 'fibonacci' in form_data else (schemaMoreDummyThanDummy if 'nothing' in form_data else otherSchema ),
            'computationStepsPackage': computation_step_package_fibonacci if 'fibonacci' in form_data else
                                        (computation_step_package_cyberpunk if 'nothing' in form_data else computation_step_package_default )
        }
        print("app created")
        db_worker.saveApplicationDictionary(app)
        print("post ended")
        return "OK", 200
    return "Not implemented", 501


@app.route('/library')
def application_add_form():
    if request.method == 'GET':
        return render_template('app_form.html')

@app.route('/library/launcher/application/<string:id>')
def get_stp_for_application(id):
    csp = db_worker.getApplicationCSP(id)
    return csp, 200


