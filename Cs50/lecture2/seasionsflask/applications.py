from flask import Flask,render_template,request,sessions
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem"

@app.route("/", methods=["POST","GET"])
def hello():
    
    if request.method == "POST":
        sessions["notes"]=[]
        note=request.form.get("notes")
        sessions["notes"].append(note)
        return render_template("main.html",notes=sessions["notes"])
    else:
        return render_template("main.html",notes=sessions["notes"])