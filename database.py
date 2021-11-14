import pymongo, json

class Database:

    instance = None

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb+srv://reka:ONPP6sc4@cluster0.eefqi.mongodb.net/test', tlsAllowInvalidCertificates=True)
        Database.instance = self

    def init_db_data(self):
        db_file = open('database.json', 'r')
        db_data = json.load(db_file)
        for i in db_data:
            print(i)
            self.client.dogs['dogs'].insert_one(i)

    def readup_db(self):
        for i in self.client.dogs['dogs'].find():
            print(i)
