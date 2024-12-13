from flask import Flask
from src.config import Config
from flask_migrate import Migrate
from src.controllers import restaurant_table
from src.models.base import db
from src.models.restaurant_table import RestaurantTable

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  
    
    db.init_app(app)
    migrate.init_app(app,db) 
    
    app.register_blueprint(restaurant_table.bp)
    
    return app

