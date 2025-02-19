from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

ma = Marshmallow()
jwt = JWTManager()
bcrypt = Bcrypt()