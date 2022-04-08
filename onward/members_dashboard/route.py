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
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        members_db = { }
        data = pandas.read_csv("onward/csv/Onward.csv")
        n = 0
        while n < len(data):
            members_db[str(data.phone_no[n])] = {
                'name': data.name[ n ],
                'card_no': data.card_no[ n ],
                'phone_no': data.phone_no[ n ],
                'shares': float(data.shares[ n ]),
                'savings': float(data.savings[ n ]),
                'kasolayo': float(data.kasolayo[n]),
                'normal_loan': float(data.normal_loan[ n ]),
                'commodity_loan': float(data.commodity_loan[n]),
                'building_loan': float(data.building_loan[n]),
                'car_loan': float(data.car_loan[n]),
                'motorcycle_loan': float(data.motorcycle_loan[n]),
                'bank': data.bank[n],
            }
            n += 1

        if user in members_db and password == 'pass':
            return render_template('/members_dashboard/dashboard.html', user=members_db[user],
                                   title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')
        else:
            return render_template('/members_dashboard/login.html', msg=f"Invalid username or password", title='ONWARD OGUN STATE LGA STAFF CICS | LOGIN')
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
                'username': data.username[n],
                'loan': (data.loan[n]).upper(),
                'loan_amount': int(data.loan_amount[n])
            })
        n += 1
    return jsonify({
            "msg": "Successful",
            "Members_data": members_db,
        })
