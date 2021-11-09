import datetime
import pymongo
from pymongo import MongoClient
from STLsensor import Sensor


cluster = MongoClient("mongodb+srv://test-script-01:gQ9MdXknoiHNRKLM@cluster0.tgn4u.mongodb.net/mfgtest?retryWrites=true&w=majority")
db = cluster["mfgtest"]
collection = db["sensors"]

cs101db = db["cs101"]
cs102db = db["cs102"]
cs103db = db["cs103"]

db_list = {
    "cs101" : cs101db,
    "cs102" : cs102db,
    "cs103" : cs103db
    }




def create_sensor(s: Sensor) -> None:
    pass
    

def get_sensor_data(MAC: str) -> Sensor:
    return collection.find_one({"_id" : MAC})
    
