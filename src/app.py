from flask import Flask
from src.config import Config, configure_app
from flask_migrate import Migrate
from src.controllers.restaurant_table import restaurant_table_controllers
from src.controllers.orders import orders_controllers
from src.controllers.auth import auth
from src.models.base import db
from src.utils import ma, bcrypt, jwt
from src.models.users import Users



migrate = Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    configure_app(app)  
    
    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app) 
    
    app.register_blueprint(restaurant_table_controllers.bp)
    app.register_blueprint(orders_controllers.bp)
    app.register_blueprint(auth.bp)
    
    return app