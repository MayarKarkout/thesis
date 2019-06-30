# main.pyFLASK_APP=/home/mayar/PycharmProjects/Thesis/thesis/__init__.py

from flask import Blueprint, request, render_template
from flask_login import login_required, current_user

from . import db

main = Blueprint('main', __name__)


@main.route('/index')
@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

