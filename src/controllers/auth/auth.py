from flask import Blueprint, request
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from src.composer.users.create_user_composer import create_user_composer


bp = Blueprint('auth',__name__,url_prefix="/auth")

@bp.route("/create_user",methods=["POST"])
def create_user():
    try:
        data = request.json
        
        use_case = create_user_composer()
        use_case.create_user(data)
        
        return {"msg": "user_created!"}, HTTPStatus.CREATED
    except Exception as exc:
        raise


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

    access_token = create_access_token(identity=username)
    return {"access_token": access_token}