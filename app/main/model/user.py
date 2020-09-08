from .. import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__="user"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50))
    surname=db.Column(db.String(50))
    numbers=relationship("PhoneNumber",cascade="all, delete-orphan")
