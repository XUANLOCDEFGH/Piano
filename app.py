from flask import Flask, render_template
from app import *
app = Flask(__name__)

@app.route("/")
def base():
    return render_template("home.html")
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/test")
def test():
    return render_template("test.html")
@app.route("/hello")
def hello():
    return render_template("hello.html")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/nhan")
def nhan():
    return render_template("nhan.html")
@app.route("/mobile")
def mobile():
    return render_template("mobile.html")
    
if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5500, debug=True)
    app.run(debug=True)
