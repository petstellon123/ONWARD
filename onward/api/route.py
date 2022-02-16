from flask import Blueprint, render_template
from flask import current_app as app

api_bp = Blueprint('api_bp', __name__,
                   template_folder='api/templates',
                   static_folder='api/static')

#create a user
# new_user = User('8134829216', 'olaoluwa', 'Adeyemi Peter', 'rouspet62@gmail.com', '08134829216',
#                 '', 80000, 20000, 100000, False, dt.now())
# db.session.add(new_user)
# db.session.commit()
#
# #create loan record
# new_loan = Loan('8134829216', 'cics34221', 70000, 'car loan', 'New', 20000, 50000, False, dt.now())
# db.session.add(new_loan)
# db.session.commit()

#querry db
# print(User.query.all()[0].email)
# print(Loan.query.all())

@api_bp.route("/")
def Home():
    return render_template("dashboard.html")