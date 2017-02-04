from flask import Flask, request, g, render_template, jsonify
from flask_mail import Mail, Message
import threading
import schedule, time
import data

app = Flask(__name__)

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'skm2159@columbia.edu'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mailing_list = []

@app.route("/index.html", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
@app.route("/", methods = ["GET", "POST"])
def homepage():
    if request.method == "GET":
        results = data.get_data()
        return render_template("index.html", facilities = results)
    else:
        results = data.get_data()
        email_address = request.form['email_form']
        mailing_list.append(email_address)
        return render_template("index.html", facilities = facilities)


@app.route("/facilities.json", methods = ["GET"])
def facilities():
    facilities = data.get_data()
    return jsonify(facilities)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404

def send_emails(recipients):
    message = Message("Test", recipients = mailing_list)
    mail.send(message)

def wait():
    done = False
    while not done:
        schedule.run_pending()
        time.sleep(3600)

if __name__ == "__main__":
    app.debug = True
    app.secret_key="Don't store this on github"
    app.run(host = '0.0.0.0', port = 8080)

    schedule.every().saturday.at("10:37").do(send_emails, args = [mailing_list])
    email_thread = threading.Thread(target = wait())
    threads.append(email_thread)
    email_thread.start()
