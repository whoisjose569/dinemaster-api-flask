from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from src.errors import error_handler

def configure_app(app: Flask):
    error_handler(app)
    app.register_blueprint()

class Config:
    SQLALCHEMY_DATABASE_URI = config('DB_URL')

 
