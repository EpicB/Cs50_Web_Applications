from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")

@app.route("/hello", methods=["POST","GET"])
def hello2():
    if request.method == "GET":
        return "Please use the form instead."
    else:   
        name=request.form.get("name")
        return render_template("2nd.html",name=name)
    