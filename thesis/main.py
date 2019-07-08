# main.pyFLASK_APP=/home/mayar/PycharmProjects/Thesis/thesis/__init__.py
import var_dump as var_dump
from flask import Blueprint, request, render_template
from flask_login import login_required, current_user

from .models import User, Profile
from . import db

main = Blueprint('main', __name__)


@main.route('/index')
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/profile', methods=['POST'])
def profile_post():

    if request.form.get('first_name') is not None and request.form.get('first_name') != "":
        current_user.profile.first_name = request.form.get('first_name')
    if request.form.get('last_name') is not None and request.form.get('last_name') != "":
        current_user.profile.last_name = request.form.get('last_name')
    if request.form.get('country') is not None and request.form.get('country') != "":
        current_user.profile.country = request.form.get('country')
    if request.form.get('city') is not None and request.form.get('city') != "":
        current_user.profile.city = request.form.get('city')
    if request.form.get('friend_id') is not None and request.form.get('friend_id') != "":
        current_user.friend_id = request.form.get('friend_id')
        friend = User.query.get(request.form.get('friend_id'))
        friend.friend_id = current_user.id

    db.session.commit()

    return render_template('profile.html')
