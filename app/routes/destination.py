from flask import Blueprint, request, jsonify

bp = Blueprint('destination', __name__, url_prefix='/api')

@bp.route('/destinations', methods=['GET', 'POST'])
def destinations():
    return jsonify({"message": "List or add destinations (mock)"})

@bp.route('/packages', methods=['GET', 'POST'])
def packages():
    return jsonify({"message": "List or add tour packages (mock)"})