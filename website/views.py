from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

#the variable is easiest to be called the same as the routine. Then pass the name of the variable as a string to Blueprint
views = Blueprint('views',__name__)

# to define a view, you are going to put the name of your blueprint. you are going to pass the url to get to this endpoint into this.
# this function will run whenever we go to this url. so in this case, root. This will be the main page since it's just a /
#these views need to be registered in our init.py
@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})