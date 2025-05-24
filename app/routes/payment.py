from flask import Blueprint, jsonify

bp = Blueprint('payment', __name__, url_prefix='/api')

@bp.route('/pay', methods=['POST'])
def pay():
    return jsonify({
        "status": "success",
        "transaction_id": "MOCK12345",
        "amount": "1000 INR"
    })