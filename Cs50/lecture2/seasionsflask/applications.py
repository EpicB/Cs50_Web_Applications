from flask import Flask,render_template,request,sessions
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem"
Session(app)

Session["note"]=[]
@app.route("/", methods=["POST","GET"])
def hello():
    if request.method == "POST":
        note=request.form.get("note")
        Session["note"].append(note)
        return render_template("main.html",notes=Session["note"])
    else:
        return render_template("main.html")