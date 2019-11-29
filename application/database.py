from app import db

class DBProvider:
    def __init__(self):
        self.applications = db.AppDatabase

    def getApplicationsDictionaty(self):
        return self.applications.find()

    def saveApplicationDictionary(self,app):
        self.applications.insert_one(app)
