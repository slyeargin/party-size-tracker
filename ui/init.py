from flask import Flask

from config import Config
from routes import init_routes

def create_app():
    app = Flask("ui")
    app.config.from_object(Config)
    init_routes(app)

    return app