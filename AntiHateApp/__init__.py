from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# for swagger openApi
swagger = Swagger(app)
# for sqlite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app) 
cors = CORS(app)

def register_blueprints():
    from AntiHateApp.controllers.api import api
    app.register_blueprint(api, url_prefix='/api')

def main():
    register_blueprints()
    print("Started application")
    # create empty DB
    db.init_app(app)
    db.create_all(app=app)
    return app
