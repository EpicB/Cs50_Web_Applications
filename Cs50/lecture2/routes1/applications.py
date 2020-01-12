from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return  render_template("3rd.html")
@app.route("/<string:name>")
def dynamic(name):
    name = name.capitalize
    return "I have {}".format(name)