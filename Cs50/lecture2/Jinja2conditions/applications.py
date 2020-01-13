import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    new_year= now.month == 1 and now.day == 1 
    new_year= True
    return  render_template("conditions.html",new_year=new_year)
#uses jinja2
#render_template looks for a template folder that has all the templates.