from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone_no = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.Text, nullable=True)
    share = db.Column(db.Integer, nullable=True)
    savings = db.Column(db.Integer, nullable=True)
    kasolayo = db.Column(db.Integer, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    changed_pass = db.Column(db.Boolean, nullable=True, default=False)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, name, phone_no, address, share, savings, kasolayo, is_admin, status, date):
        self.user_id = user_id
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.share = share
        self.savings = savings
        self.kasolayo = kasolayo
        self.is_admin = is_admin
        self.status = status
        self.date = date

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "<User {}>".format(self.user_id)

class Old_loan(db.Model):
    __tablename__ = 'old_loan'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    normal = db.Column(db.Float, nullable=False)
    building = db.Column(db.Float, nullable=False)
    car = db.Column(db.Float, nullable=False)
    commodity = db.Column(db.Float, nullable=False)
    motorcycle = db.Column(db.Float, nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)
    date = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, normal, building, car, commodity, motorcycle, completed):
        self.user_id = user_id
        self.normal = normal
        self.building = building
        self.car = car
        self.commodity = commodity
        self.motorcycle = motorcycle
        self.completed = completed

    def __repr__(self):
        return "<Old_loan {}>".format(self.user_id)

class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=False, nullable=False)
    loan_ref = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    loan_type = db.Column(db.String, nullable=False)
    transaction_type = db.Column(db.String, nullable=False)
    total_left = db.Column(db.Integer, nullable=False)
    total_paid = db.Column(db.Integer, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, loan_ref, amount, loan_type, transaction_type,  total_left, total_paid, completed, status, date):
        self.user_id = user_id
        self.loan_ref = loan_ref
        self.amount = amount
        self.loan_type = loan_type
        self.transaction_type = transaction_type
        self.total_left = total_left
        self.total_paid = total_paid
        self.completed = completed
        self.status = status
        self.date = date

    def __repr__(self):
        return "<Loan {}>".format(self.loan_ref)
