from flask.helpers import flash
from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.email import Email



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/validate", methods=["POST"])
def validate_email():
    if Email.validate_email(request.form):
        data = {
            "email": request.form["email"]
        }
        Email.save(data)
        return redirect("/success")

    else:
        return redirect("/")

@app.route("/success")
def success():
    users= Email.get_emails()
    flash("The email address you entered is a VALID email address. Thank you.")
    return render_template("success.html", users=users)