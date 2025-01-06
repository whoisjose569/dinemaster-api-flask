from flask import Flask
from decouple import config
from src.errors.error_handler import register_error_handlers
import os



def configure_app(app: Flask):
    register_error_handlers(app)
    

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = config("DB_URLA")


 
