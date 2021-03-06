from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder='static')
    app.config[ "SQLALCHEMY_DATABASE_URI" ] = "sqlite:///onward.sqlite"
    app.secret_key = "iidnfndsfjdsnvdnvjdvdjvndnjdvjd"

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        #import parts of our app
        from .api.route import api_bp
        from .members_dashboard.route import members_bp

        #register blueprints
        app.register_blueprint(api_bp, url_prefix='/api')
        app.register_blueprint(members_bp)

        db.create_all()

        return app


