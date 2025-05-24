from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.models import Partner


bp = Blueprint('partner', __name__, url_prefix='/api')

@bp.route('/partner', methods=['POST'])
def partner_form():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    company = data.get("company")
    message = data.get("message")

    # Save to database ✅
    partner = Partner(name=name, email=email, company=company, message=message)
    db.session.add(partner)
    db.session.commit()

    print(f"📝 Partner Request from {name} | {email} | {company} | {message}")
    return jsonify({"message": "Your partnership request has been received!"})
