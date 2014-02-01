from flask import render_template, redirect,url_for, g
from flask_googleauth import GoogleAuth
from models import User, ROLE_USER, ROLE_ADMIN
from app import app, db

auth = GoogleAuth(app)

def getEmail(user):
    return user.get(u'email', None)

def isCMU(email):
    return email.split('@')[1] == 'andrew.cmu.edu'

def andrewID(email):
    return email.split('@')[0]

def getAndrewID(user):
    return andrewID(getEmail(user))

@app.route('/')
def index():
    if g.user:
        email = getEmail(g.user)
        user = User.query.filter_by(email = email).first()
        if user:
            return render_template("home.html", andrewID = user.andrewID)
        elif isCMU(email):
            print andrewID(email)
            user = User(email = email, andrewID = andrewID(email))
            db.session.add(user)
            db.session.commit()
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
    return render_template("sell.html", user=getAndrewID(g.user))

@app.route('/bargain')
def bargain():
    return render_template('bargain.html')

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/users')
def users():
    userList = User.query.order_by('id desc')
    return render_template("users.html", userList = userList)

@app.route('/map')
def map():
    return render_template("map.html")

@auth.required
@app.route('/login')
def login():
    return
