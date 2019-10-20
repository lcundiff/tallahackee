
def signup(req,db):
  user_data = req.get_json
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
  #cur = db.volunteers.find()
	
  #for doc in cur:
   # print(doc)  # or do something with the document

  return True
  
