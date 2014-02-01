from flask import render_template, redirect,url_for, g
from flask_googleauth import GoogleAuth

from app import app

auth = GoogleAuth(app)

@app.route('/')
def index():
    if g.user:
        return redirect(url_for("home"))
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")
@app.route('/buy')
def buy():
    return render_template("buy.html")

@app.route('/sell')
def sell():
    return render_template("sell.html")

@auth.required
@app.route('/login')
def login():
    return
