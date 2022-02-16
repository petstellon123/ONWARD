from flask import Blueprint, render_template, url_for
from onward.model import User, db
from datetime import datetime as dt

members_bp = Blueprint('members_bp', __name__,
                       template_folder='templates',
                       static_folder='static')

#this route login user
@members_bp.route("/")
@members_bp.route("/login", methods=['GET', 'POST'])
def login():
    all_users = User.query.all()
    return render_template('/members_dashboard/login.html', title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN',
                           user=all_users[0])

#register new member
@members_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    all_users = User.query.all()
    return render_template('/members_dashboard/signup.html', title='ONWARD OGUN STATE LGA STAFF CICS | SIGN-UP',
                           user=all_users)

#dashboard
@members_bp.route('/dashboard', methods=['GET', 'POST'])
def user_dashboard():
    all_users = User.query.all()
    return render_template('/members_dashboard/dashboard.html', title='ONWARD OGUN STATE LGA STAFF CICS | DASHBOARD',
                           user=all_users[0])