from flask import Blueprint, render_template, session, redirect

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    user = session.get("user")
    if not user:
        return redirect("/login")
    return render_template("index.html", user=user)
