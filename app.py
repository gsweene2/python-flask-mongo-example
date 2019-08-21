import os
import json
import pymongo
from flask import Flask
from flask import request
app = Flask(__name__)

usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_collection_name = os.environ['MONGO_COLLECTION_NAME']

client = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@firstcluster-obuqd.mongodb.net/test?retryWrites=true&w=majority")
db = client[mongo_db_name]
collection = db[mongo_collection_name]

@app.route("/", methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 204)

@app.route('/')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
	
if __name__ == '__main__':
    app.run()
