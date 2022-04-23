from AntiHateApp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Message %r>' % self.text

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}