from application import db
from model.application import Application

class DBProvider:
    def __init__(self):
        self.applications = db.AppDatabase.Apps

    def getApplicationsDictionaty(self):
        apps = self.applications.find()
        app_dict = []
        for a in apps:
            del a['_id']
            app = Application(a)
            app_dict.append(app.__repr__())
        return app_dict

    def saveApplicationDictionary(self,app):
        self.applications.insert_one(app)

