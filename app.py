import os
import json
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")

#index.html main page
@app.route("/", methods=["GET", "POST"])
def index():
    success = False
    in_index = True

    # All flask_session based code was found by using the documentation
    # Gets username and requests token amount (Not much I can do to implement abstraction (Flask_session is extremely picky/buggy))
    if session.get("username"):
        username = session.get("username")
        user_tokens = db.execute(
            "SELECT tokens_left FROM users WHERE id=?;", session.get("user_id"))
        # Accessing the first (and only) element in the list
        user_tokens = user_tokens[0]['tokens_left']
    else:
        username = "null"
        user_tokens = 0
    return render_template("index.html", username=username, in_index=in_index, user_tokens=user_tokens)
