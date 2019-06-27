from flask import Flask, request, render_template, url_for
from validator import mart
from contactus import information

app = Flask(__name__) 

@app.route("/home")
def home3():
    return render_template("home.html")

@app.route("/main")
def home():
	return render_template("index.html")

@app.route("/result",methods=["POST"])
def output():
    ii = request.form['Item_iden']
    oi = request.form['Outlet_iden']
    result = mart(ii, oi)
    return render_template("response.html",status=int(result[0]))

@app.route("/info")
def home1():
	return render_template("about.html")

@app.route("/contact")
def home2():
	return render_template("contact.html")

@app.route("/contactus",methods=["POST"])
def info():
    name = request.form["firstname"]
    email = request.form["email"]
    country = request.form["myCountry"]
    subject = request.form["subject"]
    information(name,email,country,subject)
    return render_template("home.html")

@app.route("/dataset")
def data():
    return render_template("dataset.html")

if __name__  == "__main__":
	app.run()