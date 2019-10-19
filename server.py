@app.route('/')
def home():    
  return render_template('login.html') #this is the home page currently

if __name__ == "__main__":
  app.run(debug=True)