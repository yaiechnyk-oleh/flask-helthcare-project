import pytest
import sys
sys.path.insert(0, '')
from flask_sqlalchemy import SQLAlchemy
from app import create_app, db
from config import TestingConfig


@pytest.fixture(scope='module')
def app():
    """Create and configure a new app instance for each test."""
    _app = create_app(TestingConfig)

    ctx = _app.app_context()
    ctx.push()

    db.create_all()

    yield _app

    db.drop_all()
    ctx.pop()


@pytest.fixture(scope='module')
def client(app):
    """Create a test client for the Flask application."""
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def _db(app):
    """Yield the database object."""
    return SQLAlchemy(app)
