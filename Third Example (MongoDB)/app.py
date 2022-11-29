from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route('/initdb')
def db_init():
    client = MongoClient(
          host='test_mongodb',
          port=27017,
          username='root',
          password='pass', 
          authSource="admin")    
    
    dblist = client.list_database_names()
    
    return dblist

if __name__ == "__main__":
    app.run(host ='0.0.0.0')