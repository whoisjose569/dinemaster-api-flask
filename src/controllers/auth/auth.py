from flask import Blueprint, request
from http import HTTPStatus
from src.composer.users.create_user_composer import create_user_composer
from src.composer.users.authenticate_user_composer import authenticate_user_composer


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
    try:
        data = request.json
        
        use_case = authenticate_user_composer()
        response = use_case.authenticate_user(data)
        return response, HTTPStatus.OK
    except Exception as exc:
        raise