from flask import Blueprint, render_template, url_for, request, jsonify
import pandas
#import flask_login
from onward.model import User, db
from datetime import datetime as dt

members_bp = Blueprint('members_bp', __name__,
                       template_folder='templates',
                       static_folder='static')
# all_users = User.query.all()
# if all_users:
#     pass
# else:
#     new = User('8134829216', 'ola', 'Peter Ola', 'ola@gmail.com', '08134829216', '', 90000, 23000, 89000, False, 'Pending', dt.now())
#     db.session.add(new)
#     db.session.commit()

#this route login user
@members_bp.route("/")
@members_bp.route("/login", methods=['GET', 'POST'])
def login():
    # all_users = User.query.all()
    # if all_users:
    return render_template('/members_dashboard/login.html', title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')


#register new member
@members_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    # all_users = User.query.all()
    # if all_users:
    return render_template('/members_dashboard/signup.html', title='ONWARD OGUN STATE LGA STAFF CICS | SIGN-UP')

#dashboard
@members_bp.route('/dashboard', methods=['GET', 'POST'])
def user_dashboard():
    # all_users = User.query.all()
    # if all_users:
    return render_template('/members_dashboard/dashboard.html', title='ONWARD OGUN STATE LGA STAFF CICS | DASHBOARD')

#create users from csv file
@members_bp.route('/members', methods=['GET', 'POST'])
def members():
    members_db = []
    data = pandas.read_csv("onward/csv/members.csv")
    n = 0
    while n < len(data):
        members_db.append({
                'name': data.name[n],
                'share': int(data.share[n]),
                'savings': int(data.savings[n]),
                'id': data.id[n],
                'username': data.username[n]
            })
        n += 1
    return jsonify({
            "msg": "Successful",
            "Members_data": members_db,
        })
