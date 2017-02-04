from flask import Flask, request, g, render_template, jsonify
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
        results = data.get_data()
        names = []
        artists = []
        from_dates = []
        to_dates = []
        latitudes = []
        longitudes = []
        descriptions = []
        boroughs = []

#        for facility in results:
#            names.append(facility['name'])
#            artists.append(facility['artist'])
#            from_dates.append(facility['from_date'])
#            to_dates.append(facility['to_date'])
#            latitudes.append(facility['lat'])
#            longitudes.append(facility['lng'])
#            descriptions.append(facility['description'])
#            boroughs.append(facility['borough'])
#        return render_template("index.html", facilities = results, names = names, artists = artists, from_dates = from_dates, to_dates = to_dates, longitudes = longitudes, latitudes = latitudes, descriptions = descriptions, boroughs = boroughs)
        return render_template("index.html", facilities = results)
    else:
        email = request.form['email_form']
       # df2 = df.append({'Email': email, 'Address': "placeholder address"}, ignore_index=True)
        #print df2
        return render_template("index.html", facilities = results)
    #return render_template("index.html", facilities = results, names = names, artists = artists, from_dates = from_dates, to_dates = to_dates, longitudes = longitudes, latitudes = latitudes, descriptions = descriptions, boroughs = boroughs)


@app.route("/facilities.json", methods = ["GET"])
def facilities():
    facilities = data.get_data()
    return jsonify(facilities)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run(host = '0.0.0.0', port = 4000)
    #app.run(host=os.getenv('IP', 'O.0.0.0'), port=int(os.getenv('PORT', 8080)))