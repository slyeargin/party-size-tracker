from flask import Flask

from config import Config
from models import db
from routes import init_routes

def create_app():
    app = Flask("app")
    app.config.from_object(Config)
    db.init_app(app)
    init_routes(app)

    return app