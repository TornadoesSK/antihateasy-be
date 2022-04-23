from AntiHateApp.database.models import User, Message
from AntiHateApp import db

def user_by_name(name: str):
    return User.query.filter_by(username=name).first()

def create_user(name):
    user = User(username=name)
    exists = User.query.filter_by(username=name).first()
    if exists != None:
        return False
    
    db.session.add(user)
    db.session.commit()
    return user

def create_message(body):
    message = Message(text=body['text'], user_id=body["user_id"])
    db.session.add(message)
    db.session.commit()
    return True

def get_all_messages():
    messages = Message.query.all()
    response = list()
    for message in messages:
        response.append(message.as_dict())
    return tuple(response)