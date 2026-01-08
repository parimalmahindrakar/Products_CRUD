from flask import Flask
from extensions import db
from flask_migrate import Migrate

from src.utils.restful_app import restful_app


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.Config")
    restful_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # with app.app_context():
    # import src.models.product

    return app
