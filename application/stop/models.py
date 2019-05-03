from application import db
from application.abstractModels import Base
from sqlalchemy import Table, Integer, ForeignKey


class Stop(Base):

    __tablename__ = "stop"

    name = db.Column(db.String(144), nullable=False)
    city = db.Column(db.String(144), nullable=False)

    def __init__(self, name, city):
        self.name = name
        self.city = city
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["USER"]
