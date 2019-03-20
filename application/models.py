from application import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(20), nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    iv = db.Column(db.Integer, nullable=False)

    def __init__(self, name, cp, iv):
        self.name = name
        self.cp = cp
        self.iv = iv
