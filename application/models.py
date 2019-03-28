from application import db
from application.abstractModels import Base

class Pokemon(Base):

    name = db.Column(db.String(20), nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    iv = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, cp, iv):
        self.name = name
        self.cp = cp
        self.iv = iv
