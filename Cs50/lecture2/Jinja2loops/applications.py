from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello():
    names = ["Epic","Ahmad","Potato"]
    return render_template("loops.html",names=names)