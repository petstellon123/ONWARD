from flask import Blueprint, render_template, json, jsonify, request, flash, redirect, url_for
from onward.model import db, User, Loan, Old_loan
from datetime import datetime as dt
from flask_login import current_user, login_user
from onward import login_manager


api_bp = Blueprint('api_bp', __name__,
                   template_folder='api/templates',
                   static_folder='api/static')


#this route check user login
@api_bp.route("/login", methods=["POST"])
def login():
    datas = request.get_json()  # get json file from incoming request
    data = json.loads(datas)
    user = User.query.filter_by(user_id = data['username']).first()
    if user and user.check_password(password=data['password']):
        return jsonify({'msg': 'Successful', 'is_user': True})
    else:
        return jsonify({'msg': 'Successful', 'is_user': False})


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    flash('you must be logged in to view that page')
    return redirect(url_for('members_bp.login'))


#this route creates multiple users from csv file
@api_bp.route("/create_multiple", methods=["POST"])
def create_multiple_users():
    datas = request.get_json()  # get json file from incoming request
    data = json.loads(datas)  # convert json file to dictionary
    for pple in data['users']:
        user_check = User.query.filter_by(user_id = pple['user_id']).first()
        if user_check:
            pass
        else:
            new_user = User(pple['user_id'], pple['name'], pple['phone_no'], '', float(pple['shares']),
                            float(pple['savings']), float(pple['kasolayo']), False, 'PENDING', dt.now())
            new_user.set_password('pass')
            db.session.add(new_user)
    for lln in data['loans']:
        loan_check = Old_loan.query.filter_by(user_id = lln['user_id']).first()
        if loan_check:
            pass
        else:
            use_loan = Old_loan(lln['user_id'], float(lln['normal_loan']), float(lln['building_loan']), float(lln['car_loan']), float(lln['commodity_loan']),
                                float(lln['motorcycle_loan']), False)
            db.session.add(use_loan)
    db.session.commit()
    #print(data)
    return jsonify({"msg": "Successful"})


@api_bp.route("/")
def Home():
    return render_template("dashboard.html")