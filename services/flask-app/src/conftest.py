import pytest

from src import create_app

from src.config import TestingConfig


@pytest.fixture
def app():
    """Create a new Flask application instance for each test."""
    app = create_app(config_class=TestingConfig)
    yield app


@pytest.fixture
def client(app):
    """Provide a test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Provide a test runner for the app."""
    return app.test_cli_runner()
