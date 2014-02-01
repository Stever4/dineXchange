from flask import render_template, redirect,url_for, g
from flask_googleauth import GoogleAuth
from models import User, ROLE_USER, ROLE_ADMIN
from app import app, db
from cmu import getEmail, isCMU, andrewID, getAndrewID

auth = GoogleAuth(app)
auth.force_auth_on_every_request = True
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
            return render_template("index.html", error="authenticate")
    return render_template("index.html")

@auth.required
@app.route('/home')
def home():
    return render_template("home.html")

@auth.required
@app.route('/chat')
def chat():
    return render_template('agree.html', user=getAndrewID(g.user))

@auth.required
@app.route('/buy')
def buy():
    return render_template("buy.html", user=getAndrewID(g.user))

@auth.required
@app.route('/sell')
def sell():
    return render_template("sell.html", user=getAndrewID(g.user))

@auth.required
@app.route('/bargain')
def bargain():
    return render_template('bargain.html')

@app.route('/about')
def about():
    return render_template("about.html")

@auth.required
@app.route('/users')
def users():
    userList = User.query.order_by('id desc')
    return render_template("users.html", userList = userList)

@auth.required
@app.route('/map')
def map():
    return render_template("map.html")

@auth.required
@app.route('/login')
def login():
    return
