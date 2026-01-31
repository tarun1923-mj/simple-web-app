from flask import Flask, flash, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secretkey123"
import os
import certifi
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable not set")

client = MongoClient(
    MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client.userDB
users = db.users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = generate_password_hash(request.form['password'])

    if users.find_one({"email": email}):
        flash("User already exists", "error")
        return redirect('/')

    users.insert_one({
        "email": email,
        "password": password
    })

    flash("Registration successful. Please login.", "success")
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users.find_one({"email": email})

    if user and check_password_hash(user['password'], password):
        session['email'] = email
        return redirect('/portfolio')

    flash("Invalid email or password", "error")
    return redirect('/')

@app.route('/portfolio')
def portfolio():
    if 'email' in session:
        return render_template('portfolio.html', email=session['email'])
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app = app
