from flask import Flask, redirect, url_for
from flask_cors import CORS
from .extensions import db, login_manager, mail

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    @app.route('/')
    def home():
        return redirect(url_for('dashboard.admin_dashboard'))

    from .routes import auth, destination, admin, payment, notify, misc, contact, booking, dashboard, partner

    app.register_blueprint(dashboard.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(destination.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(notify.bp)
    app.register_blueprint(misc.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(booking.bp)
    app.register_blueprint(partner.bp)

    return app

from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    # You can implement your user loader here
    return User.query.get(int(user_id))  # Example if you have User model

class DummyUser(UserMixin):
    def __init__(self, id):
        self.id = id

