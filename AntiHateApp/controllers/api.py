from flask import Blueprint, jsonify, request

from AntiHateApp.database.models import User
from AntiHateApp.services.service import *

api = Blueprint('api', __name__)

@api.route('/user/<name>', methods=['GET'])

def get_user_by_name(name: str):
  """
  Returns user from database.
  Not cleaning input param. Pls no hack me.
  ---
  responses:
    200:
      description: user
      schema:
        type: object
        properties:
          id:
            type: integer
            required: true
          username:
            type: string
            required: true
    404:
      description: No user with given username found
  parameters:
    - name: name
      in: path
      type: string
      required: true
  """
  user = user_by_name(name)
  if (user == None):
    return create_error_message("No user with username " + name + " found.", 404)
  return jsonify(user.as_dict())

@api.route('/user', methods=['POST'])
def post_user():
  """
  Addes new user to database.
  ---
  parameters:
    - name: name
      in: body
      required: true
      type: string
      description: Unique name for user
  responses:
    200:
      description: new user added successfully
      schema:
        type: object
        properties:
          id:
            type: integer
            required: true
          username:
            type: string
            required: true
    400:
      description: user already exists
    422:
      description: missing body
  """
  name = request.get_json()

  if not name or name == "":
    return create_error_message("Missing name", 422)
  
  response = create_user(name)

  if response:
    return jsonify(response.as_dict())
  else:
    return create_error_message("User already exists", 400)

@api.route("/message", methods=["POST"])
def post_message():
  """
  Addes new message to database.
  ---
  parameters:
    - name: body
      in: body
      required: true
      schema:
        properties:
          text:
            type: string
            required: true
            description: Text, mae 1000 chars
          user_id:
            type: integer
            required: true
            desc: ID of user
  responses:
    200:
      description: new user added successfully
    422:
      description: missing body
  """
  body = request.get_json()

  if not body or body == "":
    return create_error_message("Missing body", 422)
  
  response = create_message(body)

  if response:
    return create_success_message("Messages added successfully")
  else:
    return create_error_message("I have no idea what happend", 500)

@api.route("/message/all", methods=["GET"])
def get_messages():
  """
  Returns all messages.
  ---
  responses:
    200:
      description: List of all messages
      schema:
        type: array
        items:
          type: object
          properties:
            user_id:
              type: integer
              required: true
            text:
              type: string
              required: true
  """
  messages = get_all_messages()
  return jsonify(messages), 200


def create_error_message(message: str, httpCode: int = 500):
  error_message = {"error": True, "message": message}
  return jsonify(error_message), httpCode

def create_success_message(message: str = "Success"):
  success_message = {"success": True, "message": message}
  return jsonify(success_message), 200