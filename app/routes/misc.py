from flask import Blueprint

bp = Blueprint('misc', __name__)

@bp.route('/')
def home():
    return "✅ Flask backend is running!"