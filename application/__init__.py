from flask import Flask
from pymongo_helplib import MongoClient

app = Flask(__name__, template_folder='templates')

db = MongoClient("mongodb+srv://ctcluster-ph4yr.mongodb.net/AppDatabase",
                 username='AppDatabaseUser',
                 password='plan-b-po-apps'
                 )

from application import library