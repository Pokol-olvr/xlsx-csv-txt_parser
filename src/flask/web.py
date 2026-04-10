from flask import Flask, render_template

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/dbconn")
def dbconn():
    return render_template("dbconn.html")

@app.route("/kezelo")
def kezelo():
    return render_template("kezelo.html")