# below is very basic flask application
from os import name
from flask import Flask,render_template
#from flask_cors import CORS



#referencing the app file
app=Flask("__name__")


        
#CORS(app)
#create index rout so tht when we brosw to the URL
#@app.route('/')
@app.route('/')

def index():
    
    
    return render_template("index.html")

   

if __name__=="__mani__":
    #app.run(debug=True)# this is for development
    app.run(host="0.0.0.0", port=5000)# this is for production