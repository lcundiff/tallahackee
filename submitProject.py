
def submitProject(req,db):
  print("submitting project")
  project_data = req
  # looks for nonprofit in db and then adds the project object to project array
  db.nonprofits.update_one(
    {'_id': '5dac44c9de0faf147163049a' },
    { "$push": {"projects": project_data} }, 
    upsert=False
  )
  return 'np.html'
  
