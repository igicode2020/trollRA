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
    prompt =
    username23 = username.rstrip('@andrew.cmu.edu')
    return render_template("index.html", username=username, in_index=in_index, user_tokens=user_tokens, username23=username23, prompt=prompt)

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        # Error handling
        if not request.form.get("username"):
            error = "Please enter a Username"
            return render_template("login.html", error=error)

        if not request.form.get("password"):
            error = "Please enter a password"
            return render_template("login.html", error=error)

        # Request database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?;", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            error = "Invalid Username or Password"
            return render_template("login.html", error=error)

        # Remember which user has logged in
        session['user_id'] = rows[0]['id']
        session["username"] = request.form.get("username")
        # Redirect user to home page
        return redirect("/")

    elif request.method == "GET":
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        # Error handling
        if not (username := request.form.get("username")):
            error = "Please enter a Username"
            return render_template("register.html", error=error)

        if not (password := request.form.get("password")):
            error = "Please enter a password"
            return render_template("register.html", error=error)

        if not (confirmation := request.form.get("confirm_password")):
            error = "Passwords do not match"
            return render_template("register.html", error=error)

        # Queries database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)

        # Ensures that the username  is not in database
        if len(rows) != 0:
            error = f"The username '{username}' already exists. Please choose another name."
            return render_template("register.html", error=error)

        # Ensure first password and second password are matched
        if password != confirmation:
            error = "Passwords do not match"
            return render_template("register.html", error=error)

        # Inserts username into database
        id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?);",
                        username, generate_password_hash(password))

        # Remember which user has logged in
        session["user_id"] = id
        session["username"] = username
        return redirect("/")

    elif request.method == "GET":
        return render_template("register.html")

@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")