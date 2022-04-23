from flask import Blueprint, jsonify

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