from flask import Blueprint, render_template, session, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity

home_bp = Blueprint("home", __name__)


@home_bp.route("/home")
def home():
    return render_template("index.html")


@home_bp.route("/")
def login():
    return render_template("login.html")


@home_bp.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")
