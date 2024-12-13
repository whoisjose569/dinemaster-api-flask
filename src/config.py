from flask import Flask
from decouple import config
from src.errors.error_handler import handle_exception
from werkzeug.exceptions import HTTPException

def configure_app(app: Flask):
    app.register_error_handler(HTTPException, handle_exception)
    

class Config:
    SQLALCHEMY_DATABASE_URI = config('DB_URL')

 
