
def signup(req,db):
  user_data = req
  try:
    if(user_data["user_type"] == "np"):
      db.nonprofits.insert_one({
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "website": user_data["website"],
        "projects": {},
        "volunteers": {}
      })	
      return ('profile.html')
  except:
    try:
      db.volunteers.insert_one({
        "email": user_data["email"],
        "password": user_data["password"],
        "fname": user_data["fname"],
        "lname": user_data["lname"]
      })
      return ('profile.html')
    except:
      return ('register.html')
  return ('register.html')
  #cur = db.volunteers.find()
	
  #for doc in cur:
   # print(doc)  # or do something with the document

  return True

def signin(req, db):
  user_data = req
  username = user_data["email"]
  password = user_data["password"]
  
  try:
    if(user_data["user_type"] == "np"): # Verifies login info for volunteer
     if (username == db.nonprofits.find_one({"email" : user_data["email"]}) is None):
      print("Username not found.")
      return 'sign-in.html'
    if (db.nonprofits.find_one({"password" : user_data["password"]}) is not None):
      return 'profile.html'
    else: 
      print("Password is incorrect.")
      return 'sign-in.html'
  except:
    if( db.volunteers.find_one({"email" : user_data["email"]}) is None):
      print("Username not found.")
      return 'sign-in.html'
    if (db.volunteers.find_one({"password" : user_data["password"]}) is not None):
      return 'profile.html'
    else: 
      print("Password is incorrect.")
      return 'sign-in.html'
  
  else:
    return 'sign-in.html' #should never happen

	
  
