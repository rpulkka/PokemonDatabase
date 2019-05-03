from application import db
from application.abstractModels import Base
from application.type.models import Type
from application.move.models import Move
from application.auth.models import User
from sqlalchemy.sql import text
import enum
from sqlalchemy import Integer, Enum

class Pokemon(Base):

    name = db.Column(db.String(20), nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    iv = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    fastmove_id = db.Column(db.Integer, db.ForeignKey('move.id'),
                           nullable=False)
    chargemove_id = db.Column(db.Integer, db.ForeignKey('move.id'),
                           nullable=False)

    first_type_id = db.Column(db.Integer, nullable=False)
    second_type_id = db.Column(db.Integer, nullable=False)

    fastmove = db.relationship("Move", foreign_keys=[fastmove_id])
    chargemove = db.relationship("Move", foreign_keys=[chargemove_id])

    def __init__(self, name, cp, iv, fastmove_id, chargemove_id, first_type_id, second_type_id):
        self.name = name
        self.cp = cp
        self.iv = iv
        self.fastmove_id = fastmove_id
        self.chargemove_id = chargemove_id
        self.first_type_id = first_type_id
        self.second_type_id = second_type_id

    @staticmethod
    def find_highest_cp():
        stmt = text("select * from pokemon order by cp desc limit 1")
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"name":row[3], "cp":row[4], "iv":row[5], "trainer":row[6]})
        return response

    @staticmethod
    def find_highest_iv():
        stmt = text("select * from pokemon order by iv desc limit 1")
        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({"name":row[3], "cp":row[4], "iv":row[5], "trainer":row[6]})
        return response

    def most_common_move_of_trainer(current):

        if current == -1:
            return ""

        stmt1 = text("SELECT fastmove_id FROM Pokemon, Account WHERE Pokemon.account_id =:x group by fastmove_id ORDER BY COUNT(*) desc limit 1;").params(x = current)
        res1 = db.engine.execute(stmt1)

        num1 = 1
        for iter in res1:
            num1 = iter[0]

        stmt2 = text("SELECT chargemove_id FROM Pokemon, Account WHERE Pokemon.account_id =:x group by chargemove_id ORDER BY COUNT(*) desc limit 1;").params(x = current)
        res2 = db.engine.execute(stmt2)

        num2 = 1
        for iter in res2:
            num2 = iter[0]

        num3 = 0

        if num1 >= num2:
            num3 = num1
        else:
            num3 = num2

        stmt3 = text("SELECT name FROM Move WHERE Move.id =:x;").params(x = num3)
        res3 = db.engine.execute(stmt3)

        final = ""
        for iter in res3:
            final = iter[0]

        return final

    def fast_move_name(self):
        movename = Move.getNameById(self.fastmove_id)
        return movename

    def charge_move_name(self):
        movename = Move.getNameById(self.chargemove_id)
        return movename

    def first_type_name(self):
        typename = Type(self.first_type_id).name
        return typename

    def second_type_name(self):
        typename = Type(self.second_type_id).name
        return typename
