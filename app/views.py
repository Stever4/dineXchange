from flask import render_template, redirect,url_for, g
from flask_googleauth import GoogleAuth

from app import app

auth = GoogleAuth(app)

def getEmail(user):
    return user.get(u'email', None)

def isCMU(email):
    return email.split('@')[1] == 'andrew.cmu.edu'

def andrewID(email):
    return email.split('@')[0]

@app.route('/')
def index():
    if g.user:
        email = getEmail(g.user)
        if isCMU(email):
            print andrewID(email)
            return render_template("home.html", andrewID = andrewID(email))
        else:
            return redirect(url_for("error"))
    return render_template("index.html")

@app.route('/error')
def error():
    return ":("

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/buy')
def buy():
    return render_template("buy.html")

@app.route('/sell')
def sell():
    return render_template("sell.html", user=g.user)

@app.route('/bargain')
def bargain():
    return render_template('bargain.html')

@app.route('/about')
def about():
    return render_template("about.html")

@auth.required
@app.route('/login')
def login():
    return
