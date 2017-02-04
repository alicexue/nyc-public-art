from flask import Flask, request, g, render_template
import sqlite3
import os
import data
#import pandas as pd

app = Flask(__name__)

columnsthis = ['Email', 'Address']
#df = pd.DataFrame(columns=columnsthis)

@app.route("/index.html", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        facilities = data.get_data()
        latitudes = []
        longitudes = []
        for facility in facilities:
            latitudes = facility['lat']
            longitudes = facility['lng']
        return render_template("index.html", latitudes = latitudes, longitudes = longitudes)
    else:
        email = request.form['email_form']
       # df2 = df.append({'Email': email, 'Address': "placeholder address"}, ignore_index=True)
        #print df2
    return render_template("index.html", facilities = facilities)

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.run(host=os.getenv('IP', 'O.0.0.0'), port=int(os.getenv('PORT', 8080)))