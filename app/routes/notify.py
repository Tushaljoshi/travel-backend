from flask import Blueprint, jsonify

bp = Blueprint('notify', __name__, url_prefix='/api/notify')

@bp.route('/email', methods=['POST'])
def email_notify():
    return jsonify({"message": "Mock email sent"})

@bp.route('/sms', methods=['POST'])
def sms_notify():
    return jsonify({"message": "Mock SMS sent"})