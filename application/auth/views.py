from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, AccountForm

from flask_login import login_user, logout_user

@app.route("/new_account/", methods=["GET"])
def account_form():
    return render_template("auth/new_account.html", form = AccountForm())

@app.route("/new_account", methods=["POST"])
def account_create():
    form = AccountForm(request.form)

    if not form.validate():
        return render_template("auth/new_account.html", form = form)

    u = User(request.form.get("username"), request.form.get("username"), request.form.get("password"))
    db.session().add(u)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  
