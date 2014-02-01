from flask import render_template
from app import app
from forms import LoginForm

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buy')
def buy():
    return render_template("buy.html")

@app.route('/sell')
def sell():
    return render_template("sell.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/')
    return render_template('login.html',
                            title = 'Sign In',
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])

