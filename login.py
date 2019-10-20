
def signup(req,db):
  user_data = req
  if(user_data["user_type"] == "volunteer"):
    db.volunteers.insert_one({
      "email":'lcundiff@ufl.edu', 
  	  "password": 'fsuhack',
      "fname": 'Logan',
      "lname": 'Cundiff'
  })
  elif(user_data["user_type"] == "np"):
    db.nonprofits.insert_one({
      "email":'lcundiff@ufl.edu',
      "password": 'fsuhack',
	    "name": 'Logan',
      "projects": {[]},
      "volunteers": {[]}
  	})	
  return ('profile.html')
  #cur = db.volunteers.find()
	
  #for doc in cur:
   # print(doc)  # or do something with the document

  return True

def signin(req, db):
  user_data = req
  username = user_data["email"]
  password = user_data["password"]
  
  if(user_data["user_type"] == "volunteer"): # Verifies login info for volunteer
    if(username == db.volunteers.find_one({"email" : user_data["email"]})):
      print("Username not found.")
      return False
    if (password == db.volunteers.find_one({"password" : user_data["password"]})):
      return True
    else: 
      print("Password is incorrect.")
      return False


  elif(user_data["user_type"] == "np"): # Verifies login info for nonprofit
    if (username == db.nonprofits.find_one({"email" : user_data["email"]})):
      print("Username not found.")
      return False
    if (password == db.nonprofits.find_one({"password" : user_data["password"]})):
      return True
    else: 
      print("Password is incorrect.")
      return False
	
  
