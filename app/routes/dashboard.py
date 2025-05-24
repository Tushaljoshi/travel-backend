from flask_login import current_user
from flask import Blueprint, render_template
from app.models.models import Contact, Partner, Booking

bp = Blueprint('dashboard', __name__, url_prefix='/admin')

@bp.route('/dashboard')
def admin_dashboard():
    try:
        current_user  # just reference to prevent Flask-Login error
    except:
        pass

    contacts = Contact.query.all()
    partners = Partner.query.all()
    bookings = Booking.query.all()
    return render_template('dashboard.html', contacts=contacts, partners=partners, bookings=bookings)
