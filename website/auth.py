from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)        # Blueprint of the application.

# About
@auth.route('/about')
def about():
    return render_template("about.html")
    
# Log in
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True)

# Log out
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Sign up
@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        if email.indexOf('@') != -1:
            flash('Input is not a valid email.', category = 'error')
        elif password < 7:
            flash('Password must be at least 7 characters.', category = 'error') 
        elif password != password_confirm:
            flash('Password does not match.', category = 'error') 
        else:
            flash('Account created!', category='success')

    return render_template("signup.html")


