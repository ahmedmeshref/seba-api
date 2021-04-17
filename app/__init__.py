# app generator 
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_migrate import Migrate


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(Config)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)


    with app.app_context():
        # import blueprints
        from .venues import venues
        from .errors import errors


        # register blueprints
        app.register_blueprint(venues.venues)
        app.register_blueprint(errors.error)

        return app







