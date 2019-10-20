
def submitProject(req,db):
  print("submitting project")
  project_data = req
  # looks for nonprofit in db and then adds the project object to project array
  db.update_one(
    {'_id': project_data['np_id'] },
    { "$push": {"projects": project_data} }, 
    upsert=False
  )
  return True
  
