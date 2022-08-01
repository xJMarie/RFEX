from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)        # Blueprint of the application.

# About
@auth.route('/about')
def about():
    return render_template("about.html")
    
# Log in
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('registerEmail')
        firstName = request.form.get('registerFName')
        lastName = request.form.get('registerLName')
        password = request.form.get('registerPassword')
        password_confirm = request.form.get('registerRepeatPassword')
        print(email)
        if len(email) < 4:
            flash('Email is less than 4 characters', category = 'error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category = 'error') 
        elif password != password_confirm:
            flash('Password does not match.', category = 'error') 
        else:
            flash('Account created!', category='success')
    else:
        data = request.form
        print(data)
        print("JABOL")
    return render_template("login.html", boolean = True)

# Log out
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Sign up
@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    print("PASS1")

    return render_template("signup.html")


