from . import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_no = db.Column(db.String, unique=True, nullable=False)
    address = db.Column(db.Text, nullable=True)
    share = db.Column(db.Integer, nullable=True)
    savings = db.Column(db.Integer, nullable=True)
    kasolayo = db.Column(db.Integer, nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, password, name, email, phone_no, address, share, savings, kasolayo, is_admin, status, date):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.address = address
        self.share = share
        self.savings = savings
        self.kasolayo = kasolayo
        self.is_admin = is_admin
        self.status = status
        self.date = date

    def __repr__(self):
        return "<User {}>".format(self.user_id)


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
