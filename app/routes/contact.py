from flask import Blueprint, request, jsonify
from app import db
from app.models.models import Contact

bp = Blueprint('contact', __name__, url_prefix='/api')

@bp.route('/contact', methods=['POST'])
def contact():
    data = request.form
    contact = Contact(
        name=data.get("name"),
        email=data.get("email"),
        message=data.get("message")
    )
    db.session.add(contact)
    db.session.commit()
    return jsonify({"message": "Message received successfully!"})
