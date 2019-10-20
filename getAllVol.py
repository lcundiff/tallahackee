
def getAllVol(db):
  print("getting all volunteers")

  # gathers all volunteer data
  vol_data = db.volunteers.find()
  return vol_data