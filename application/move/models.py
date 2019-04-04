from application import db
from application.abstractModels import Base


class Move(Base):

    __tablename__ = "move"

    name = db.Column(db.String(144), nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    chargeMove = db.Column(db.Boolean, nullable=False)
    bars = db.Column(db.Integer, nullable=True)

    def __init__(self, name, damage, chargeMove, bars):
        self.name = name
        self.damage = damage
        self.chargeMove = chargeMove
        self.bars = bars
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True