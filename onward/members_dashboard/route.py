import json
from flask import Blueprint, render_template, url_for, request, jsonify, redirect
import requests
import pandas
from flask_login import login_user, login_required, current_user, logout_user
from onward.model import User, db, Old_loan
from datetime import datetime as dt

members_bp = Blueprint('members_bp', __name__,
                       template_folder='templates',
                       static_folder='static')
# all_users = User.query.all()
# if all_users:
#     print(all_users)
#     pass
# else:
#     new = User('8134829216', 'ola', 'Peter Ola', 'ola@gmail.com', '08134829216', '', 90000, 23000, 89000, False, 'Pending', dt.now())
#     db.session.add(new)
#     db.session.commit()

#this route login user
@members_bp.route("/")
@members_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        info = {
            'username': user,
            'password': password
        }
        user_log = json.dumps(info)
        host = request.host_url
        send = requests.post(f'{host}{url_for("api_bp.login")}', json=user_log)
        response = send.json()
        if response['is_user']:
            user = User.query.filter_by(user_id = user).first()
            login_user(user)
            if user.changed_pass:
                return redirect(url_for('members_bp.user_dashboard'))
            else:
                return redirect(url_for('members_bp.change_password'))
        else:
            msg = "invalid username or password"
            return render_template('/members_dashboard/login.html', msg=msg, title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')
    return render_template('/members_dashboard/login.html', title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')


#register new member
@members_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    # all_users = User.query.all()
    # if all_users:
    return render_template('/members_dashboard/signup.html', title='ONWARD OGUN STATE LGA STAFF CICS | SIGN-UP')

#dashboard
@members_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def user_dashboard():
    loan = Old_loan.query.filter_by(user_id=current_user.user_id).first()
    return render_template('/members_dashboard/dashboard.html', user=current_user, loan=loan, title='ONWARD OGUN STATE LGA STAFF CICS | DASHBOARD')

@members_bp.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == "POST":
        password = request.form[ 'password' ]
        confirm_pass = request.form['confirm_password']
        if password == confirm_pass:
            user = User.query.filter_by(user_id = current_user.user_id).first()
            user.set_password(password)
            user.changed_pass = True
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('members_bp.user_dashboard'))
        else:
            msg = 'Password and Confirm password does not match.'
            return render_template('members_dashboard/change_pass.html', msg=msg, title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')
    return render_template('members_dashboard/change_pass.html', title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')





@members_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('members_bp.login'))

#create users from csv file
# @members_bp.route('/members', methods=['GET', 'POST'])
# def members():
#     members_db = []
#     data = pandas.read_csv("onward/csv/members.csv")
#     n = 0
#     while n < len(data):
#         members_db.append({
#                 'name': data.name[n],
#                 'share': int(data.share[n]),
#                 'savings': int(data.savings[n]),
#                 'id': data.id[n],
#                 'username': data.username[n],
#                 'loan': (data.loan[n]).upper(),
#                 'loan_amount': int(data.loan_amount[n])
#             })
#         n += 1
#     return jsonify({
#             "msg": "Successful",
#             "Members_data": members_db,
#         })
