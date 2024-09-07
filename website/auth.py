from flask import Blueprint,render_template

#the variable is easiest to be called the same as the routine. Then pass the name of the variable as a string to Blueprint
auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    # you can pass variables to your templates to be used for display purposes like so: here we are passing text
    return render_template('login.html', boolean=False)

@auth.route('/logout')
def logout():
    return "<p>Logout</P>"

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')
