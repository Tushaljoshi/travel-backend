from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/api')

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()  # <-- IMPORTANT
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    print(f"Signup: {name}, {email}")
    return jsonify({"message": "Signup success (mock)"})


@bp.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login success (mock)"})