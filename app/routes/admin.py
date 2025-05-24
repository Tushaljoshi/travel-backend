from flask import Blueprint, jsonify

bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@bp.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({
        "users": 100,
        "bookings": 45,
        "revenue": 12000,
        "disputes": 2
    })