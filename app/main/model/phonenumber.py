from .user import User
from .. import db
from sqlalchemy import ForeignKey

class PhoneNumber(db.Model):
    __tablename__="phonenumber"

    id=db.Column(db.Integer, primary_key=True)
    uid=db.Column(db.Integer, ForeignKey(User.id))
    phoneNumber=db.Column(db.String(50))
    type=db.Column(db.String(50))
    