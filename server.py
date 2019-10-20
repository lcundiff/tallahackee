from flask import Flask
import os
from flask import render_template
from flask import request
from pymongo import MongoClient
from login import *
from submitProject import *
from getMatches import *

client = MongoClient('mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority')
global db
db = client.get_database('hackershelping')


#mongodb+srv://hackershelping:hackfsu@hackershelping-akpvf.gcp.mongodb.net/test?retryWrites=true&w=majority

app = Flask(__name__)

@app.route('/')
def home():    
  return render_template('sign-in.html') #this is the home page currently

@app.route('/login', methods=['GET', 'POST'])
def loginRoute():    
  print("logging in")
  return render_template(signin(request.form,db)) #this is the home page currently

@app.route('/load_signup_screen', methods=['GET', 'POST'])
def signupScreenRoute():    
  return render_template('register.html') # brings user to sign up screen

@app.route('/signup', methods=['GET', 'POST'])
def signupRoute():    
  #print(vars(request))
  return render_template(signup(request.form,db)) #this is the home page currently

@app.route('/submitProject', methods=['GET', 'POST'])
def submitProjectRoute():    
  return submitProject(request.form,db)

@app.route('/getMatches', methods=['GET', 'POST'])
def getMatchesRoute(req):    
  return getMatches(req,db)



if __name__ == "__main__":
  app.run(debug=True)
