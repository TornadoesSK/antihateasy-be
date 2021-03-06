from AntiHateApp.database.models import User, Message
from AntiHateApp import db
import requests

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
    force = body['force']
    hateful = checkHate(body['text'])
    if not force:
        if hateful:
            return False

    message = Message(text=body['text'], user_id=body["user_id"], hate=hateful)
    db.session.add(message)
    db.session.commit()
    return True

def get_all_messages():
    messages = Message.query.order_by(Message.id.desc()).all()
    response = list()
    for message in messages:
        name = User.query.filter_by(id=message.user_id).first().username
        response.append({"content": message.text, "name": name, "hate": message.hate})
    return tuple(response)

def checkHate(text: str):
    response = requests.post('http://localhost:6969/gettextsentiment', json = {"tweet": text}).json()
    return response['hide']