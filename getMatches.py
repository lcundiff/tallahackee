
def getMatches(req,db):
  print("submitting project")
  match_data = req.get_json()
  # looks for nonprofit in db and then adds the project object to project array
  db.get(
    {'email': project_dat['email'] },
    { "$push": {"projects": project_data} }, 
    upsert=False
  )
  return True
  
