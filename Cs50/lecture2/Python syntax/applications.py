from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route("/david")
def david():
    return "Hello, david!"    
#cd lecture2
#set FLASK_APP=applications.py
#flask run
#export FLASK_APP=applications.py