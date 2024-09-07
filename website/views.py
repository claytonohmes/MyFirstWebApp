from flask import Blueprint, render_template

#the variable is easiest to be called the same as the routine. Then pass the name of the variable as a string to Blueprint
views = Blueprint('views',__name__)

# to define a view, you are going to put the name of your blueprint. you are going to pass the url to get to this endpoint into this.
# this function will run whenever we go to this url. so in this case, root. This will be the main page since it's just a /
#these views need to be registered in our init.py
@views.route('/')
def home():
    return render_template("home.html")