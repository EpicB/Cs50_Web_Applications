from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    headline="hello,world"
    return  render_template("variables.html",headline=headline)
