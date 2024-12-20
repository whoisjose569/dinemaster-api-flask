import pytest
from src.app import create_app
from src.app import db

@pytest.fixture
def app():
    app = create_app(test_config=True)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()