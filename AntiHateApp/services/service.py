from AntiHateApp.database.models import User
from AntiHateApp import db

def user_by_name(name: str):
    return User.query.filter_by(username=name).first()

def create_user(body):
    user = User(username=body['name'], email=body['email'])
    exists = User.query.filter_by(username=body['name']).first()
    if exists != None:
        return False
    print(exists)
    db.session.add(user)
    db.session.commit()
    return True