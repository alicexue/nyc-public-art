from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/index.html", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def homepage():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.run(host=os.getenv('IP', 'O.0.0.0'), port=int(os.getenv('PORT', 8080)))