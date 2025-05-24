from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    message = db.Column(db.Text)

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    company = db.Column(db.String(150))
    message = db.Column(db.Text)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checkin = db.Column(db.String(20))
    checkout = db.Column(db.String(20))
    guests = db.Column(db.String(10))