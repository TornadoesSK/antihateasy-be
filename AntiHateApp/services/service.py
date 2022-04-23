from AntiHateApp.database.models import User, Message
from AntiHateApp import db

def user_by_name(name: str):
    return User.query.filter_by(username=name).first()

def create_user(body):
    user = User(username=body['name'])
    exists = User.query.filter_by(username=body['name']).first()
    if exists != None:
        return False
    
    db.session.add(user)
    db.session.commit()
    return user.id

def create_message(body):
    message = Message(text=body['text'], user_id=body["userId"])
    db.session.add(message)
    db.session.commit()
    return True

def get_all_messages():
    messages = Message.query.all()
    response = list()
    for message in messages:
        response.append(message.as_dict())
    return tuple(response)