from application import db
from model.application import Application

class DBProvider:
    def __init__(self):
        self.applications = db.AppDatabase.Apps

    def getApplicationsDictionary(self):
        apps = self.applications.find()
        app_dict = []
        for a in apps:
            del a['_id']
            try:
                del a['computationStepsPackage']
            except Exception:
                print("nothing interestiong here")#Fuck it
            app = Application(a)
            app_dict.append(app.__repr__())
        return app_dict

    def saveApplicationDictionary(self,app):
        self.applications.insert_one(app)

    def getApplicationCSP(self, app_id):
        app = self.applications.find_one({"id":app_id})
        return app['computationStepsPackage']