
def getAllNP(db):
  print("getting all non-profits")

  # gathers all non-profit data
  np_data = db.nonprofits.find()
  return np_data
  
