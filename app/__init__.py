# app generator 
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.models import setup_db

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    with app.app_context():
        setup_db(app)

        # import blueprints
        from .venues import venues
        from .errors import errors
        from .shows import shows
        from .users import users

        # register blueprints
        app.register_blueprint(venues.venues)
        app.register_blueprint(shows.shows)
        app.register_blueprint(errors.error)
        app.register_blueprint(users.users)

        return app







