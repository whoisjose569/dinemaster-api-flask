from flask import Blueprint, request
from http import HTTPStatus
from src.repositories.restaurant_table.restaurant_table_repository import _create_restaurant_table, _check_table_number_exists
from src.presenters.restaurant_table.restaurant_table_presenter import format_table_presenter

bp = Blueprint('restaurant_table', __name__, url_prefix='/tables')

@bp.route('/', methods=["POST"])
def create_restaurant_table():
    try:
        data = request.json
        _check_table_number_exists(data)
        response = _create_restaurant_table(data) 
        return format_table_presenter(response), HTTPStatus.CREATED
    except Exception as exc:
        raise