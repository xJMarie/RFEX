from flask import Blueprint, render_template

views = Blueprint('views', __name__)        # Blueprint of the application.

@views.route('/')
def home():
    #TODO User (Database)
    user=True;
    return render_template("home.html", user=user)