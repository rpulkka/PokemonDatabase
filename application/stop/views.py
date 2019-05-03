from flask import render_template, request, redirect, url_for
from application import app, db, login_required
from flask_login import current_user
from application.stop.models import Stop
from application.stop.forms import StopForm

@app.route("/stops", methods=["GET"])
def stopindex():

    return render_template("stop/stoplist.html", stoplist = Stop.query.all())

@app.route("/new_stop", methods=["GET"])
@login_required(role="USER")
def stop_form():
    form = StopForm()

    return render_template("stop/new_stop.html", form = form)

@app.route("/new_stop", methods=["POST"])
@login_required(role="USER")
def stop_create():
    form = StopForm(request.form)

    if not form.validate():
        return render_template("stop/new_stop.html", form = form)

    s = Stop(request.form.get("name"), request.form.get("city"))
    db.session().add(s)
    db.session().commit()
    return redirect(url_for("stopindex"))

@app.route("/stop/<stop_id>", methods=["GET"])
def stop_view(stop_id):
    stop = Stop.query.get(stop_id)
    return render_template("stop/view_stop.html", stop = stop)

@app.route("/update_stop/<stop_id>", methods=["GET"])
@login_required(role="USER")
def stop_update_form(stop_id):
    stop = Stop.query.get(stop_id)
    form = StopForm()
    form.name.data = stop.name
    form.city.data = stop.city
    return render_template("stop/update_stop.html", form = form, stop = stop)

@app.route("/update_stop/<stop_id>", methods=["POST"])
@login_required(role="USER")
def stop_update(stop_id):
    form = StopForm(request.form)

    if not form.validate():
        return render_template("stop/update_stop.html", form = form)

    s = Stop.query.get(stop_id)
    s.name = request.form.get("name")
    s.city = request.form.get("city")

    db.session().commit()
    return redirect(url_for("stopindex"))

@app.route("/delete_stop/<stop_id>/", methods=["POST"])
@login_required(role="USER")
def stop_delete(stop_id):
    Stop.query.filter_by(id=stop_id).delete()
    db.session().commit()
    return redirect(url_for("stopindex"))
