from flask import Flask
import os
from flask import render_template

from pymongo import MongoClient
client = MongoClient('mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority')

def my_function(mydb):
    db = client.get_database(mydb)
    return db.collection.find().count()

print(my_function('my_database'))

#mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority



app = Flask(__name__)

@app.route('/')
def home():    
  return render_template('sign-in.html') #this is the home page currently

if __name__ == "__main__":
  app.run(debug=True)