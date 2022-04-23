from flask import Flask
from AntiHateApp.controllers.api import api
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

def register_blueprints():
    app.register_blueprint(api, url_prefix='/api')

def main():
    register_blueprints()
    print("Started application")
    return app
