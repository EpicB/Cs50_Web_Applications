from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")

@app.route("/more")
def hello2():
    return render_template("2nd.html")   