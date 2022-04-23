from flask import Blueprint, jsonify, request

from AntiHateApp.database.models import User
from AntiHateApp.services.service import *

api = Blueprint('api', __name__)

@api.route('/test/<name>', methods=['GET'])
def get_test(name: str):
    """
    Example endpoint returning a list of colors by palette
    This is using docstrings for specifications.
    ---
    responses:
      200:
        description: A list of colors (may be filtered by palette)
    parameters:
      - name: name
        in: path
        type: string
    """
    return jsonify("Hello " + name + "!")

@api.route('/user/<name>', methods=['GET'])
def get_user_by_name(name: str):
  """
  Returns user from database.
  Not cleaning input param. Pls no hack me.
  ---
  responses:
    200:
      description: user
    404:
      description: No user with given username found
  parameters:
    - name: username of user
      in: path
      type: string
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
    - name: body
      in: body
      required: true
      schema:
        properties:
          name:
            type: string
            description: Unique name for user
          email:
            type: string
            desc: Unique email for user
  responses:
    200:
      description: new user added successfully
    400:
      description: user already exists
    422:
      description: missing body
  """
  body = request.get_json()

  if not body or body == "":
    return create_error_message("Missing body", 422)
  
  response = create_user(body)

  if response:
    return success_message()
  else:
    return create_error_message("User already exists", 400)


def create_error_message(message: str, httpCode: int = 500):
  error_message = {"error": True, "message": message}
  return jsonify(error_message), httpCode

def success_message(message = "Success"):
  success_message = {"success": True, "message": message}
  return jsonify(success_message), 200