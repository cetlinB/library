from application import db

class DBProvider:
    def __init__(self):
        self.applications = db.AppDatabase.Apps

    def getApplicationsDictionaty(self):
        apps = self.applications.find()
        app_dict = []
        for a in apps:
            del a['_id']
            app_dict.append(a)
        return app_dict

    def saveApplicationDictionary(self,app):
        self.applications.insert_one(app)

