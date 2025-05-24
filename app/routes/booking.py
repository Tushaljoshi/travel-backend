from flask import Blueprint, request, jsonify
from app import db
from app.models.models import Booking

bp = Blueprint('booking', __name__, url_prefix='/api')

@bp.route('/book', methods=['POST'])
def book():
    data = request.form
    booking = Booking(
        checkin=data.get('checkin'),
        checkout=data.get('checkout'),
        guests=data.get('guests')
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({"message": "Booking saved"})