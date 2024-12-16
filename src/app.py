from flask import Flask
from src.config import Config, configure_app
from flask_migrate import Migrate
from src.controllers.restaurant_table import restaurant_table_controllers
from src.models.base import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    configure_app(app)  
    
    db.init_app(app)
    migrate.init_app(app,db) 
    
    app.register_blueprint(restaurant_table_controllers.bp)
    
    return app

