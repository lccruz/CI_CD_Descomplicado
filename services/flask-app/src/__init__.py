import os

from flask import Flask


def create_app(config_class=None):
    """Create app."""

    if config_class is None:
        config_class = os.environ.get(
            'APP_SETTINGS', 'src.config.ProductionConfig'
        )

    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        from .api import api

        app.register_blueprint(api.api_bp, url_prefix='/api')

    @app.route('/')
    def health_check():
        return 'Hello'

    return app
