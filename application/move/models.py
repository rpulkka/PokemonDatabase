from application import db
from application.abstractModels import Base
from application.type.models import Type
from sqlalchemy.sql import text
import enum
from sqlalchemy import Integer, Enum

class Move(Base):

    __tablename__ = "move"

    name = db.Column(db.String(144), nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    chargemove = db.Column(db.Integer, nullable=False)
    bars = db.Column(db.Integer, nullable=True)
    first_type_id = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, damage, chargemove, bars, first_type_id):
        self.name = name
        self.damage = damage
        self.chargemove = chargemove
        self.bars = bars
        self.first_type_id = first_type_id
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def getByName(targetName):
        stmt = text("select id from move where name=:x;").params(x = targetName)
        target = db.engine.execute(stmt)
        return target

    @staticmethod
    def getNameById(targetId):
        stmt = text("select * from move where id=:x;").params(x = targetId)
        res = db.engine.execute(stmt)
        target = [row for row in res]
        targetnames = [(row.name) for row in target]
        return targetnames[0]

    @staticmethod
    def allFastMoves():
        stmt = text("select * from move where chargemove = 0;")
        res = db.engine.execute(stmt)
        allFast = [row for row in res]
        return allFast

    @staticmethod
    def allChargedMoves():
        stmt = text("select * from move where chargemove = 1;")
        res = db.engine.execute(stmt)
        allCharged = [row for row in res]
        return allCharged

    def first_type_name(self):
        typename = Type(self.first_type_id).name
        return typename

    def isChargeMoveBoolean(self):
        if self.chargemove == 1:
            return True
        else:
            return False

    def canDelete(self, userid):
        stmt = text("select * from pokemon where chargemove_id =:x or fastmove_id =:x;").params(x = self.id)
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append(row[6])

        for trainer in response:
            if trainer != userid:
                return False

        return True

    def destructor(self):
        stmt = text("delete from pokemon where chargemove_id =:x or fastmove_id =:x;").params(x = self.id)
        db.engine.execute(stmt)
        return True