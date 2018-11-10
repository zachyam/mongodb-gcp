import os
import urllib3
import sys
import time
import requests
from pymongo import MongoClient
from secrets import mongo_user, mongo_pass

def save_to_db(r, time):
    mongo_url = 'mongodb://'+ mongo_user +':' + mongo_pass + 'u@mongodb-gcp-test-shard-00-00-ngczr.gcp.mongodb.net:27017,mongodb-gcp-test-shard-00-01-ngczr.gcp.mongodb.net:27017,mongodb-gcp-test-shard-00-02-ngczr.gcp.mongodb.net:27017/test?ssl=true&replicaSet=mongodb-gcp-test-shard-0&authSource=admin&retryWrites=true'
    client = MongoClient(mongo_url)
    db=client.api
    api_call = {
                'timestamp' : time,
                'request' : r.status_code,
                'response': r.text
               }
    result=db.apicalls.insert_one(api_call)


def main():
    random_url = random.choice(url_list)
    url = 'http://localhost:9090'
    r = requests.get(url)
    try:
        save_to_db(r, int(time.time()))
    except:
        print("Error saving to database")

main()
