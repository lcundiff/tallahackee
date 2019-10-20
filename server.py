from flask import Flask
import os
from flask import render_template
from pymongo import MongoClient
from login import *
from submitProject import *
from getMatches import *

global db


def getDB(client):
  db = client.get_database('hackershelping')
  #print("db check: ",db.collection.find({}))

    #return db.collection.find().count


#mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority

app = Flask(__name__)

@app.route('/')
def home():    
  return render_template('sign-in.html') #this is the home page currently

@app.route('/load_signup_screen', methods=['GET', 'POST'])
def signupScreenRoute():    
  return render_template('register.html') # brings user to sign up screen

@app.route('/signup', methods=['GET', 'POST'])
def signupRoute(req):    
  return signup(req,db) #this is the home page currently

@app.route('/submitProject', methods=['GET', 'POST'])
def submitProjectRoute(req):    
  return submitProject(req,db)

@app.route('/getMatches', methods=['GET', 'POST'])
def getMatchesRoute(req):    
  return getMatches(req,db)



if __name__ == "__main__":
  client = MongoClient('mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority')
  getDB(client)
  app.run(debug=True)
