from application import db
from application.abstractModels import Base
from sqlalchemy.sql import text

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

