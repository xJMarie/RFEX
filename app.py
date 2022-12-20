from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# Database
# client = pymongo.MongoClient('localhost', 27017)
# db = client.rfex

# Routes
from user import routes

# Landing page
@app.route('/')
def home():
    return render_template('map.html')

# Sign in and sign up page
@app.route('/signin_up/')
def signin_up():
    return render_template('signin_up.html')

# About page
@app.route('/about/')
def about():
    return render_template('about.html')

# Settings page

app.run(debug=True)     # To run the program