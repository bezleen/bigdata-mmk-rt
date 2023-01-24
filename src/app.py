from flask import Flask
# import logging
# import logging.config

from .config import DefaultConfig
from .extensions import (
    socketio,
    mdb
)


def create_app():
    app = Flask(__name__)
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    config_namespace()
    return app


def config_namespace():
    from .events import (
        MMK
    )

    socketio.on_namespace(MMK("/events/mmk"))


def configure_app(app):
    app.config.from_object(DefaultConfig)


def configure_extensions(app):
    socketio.init_app(app, allow_upgrades=True)
    mdb.init_app(app)
    # logging
    # logging.config.dictConfig(LoggingConfig.LOGGING_CONFIG)
    return


def configure_blueprints(app):
    """Configure blueprints in views."""
    from src.api import DEFAULT_BLUEPRINTS as blueprints
    for blueprint in blueprints:
        app.register_blueprint(
            blueprint,
            url_prefix=f'/v1/api/{blueprint.url_prefix}'
        )
