from flask import Blueprint, request
from http import HTTPStatus
from src.composer.restaurant_table.create_table_composer import create_table_composer
from src.composer.restaurant_table.list_table_composer import list_table_composer
from src.composer.restaurant_table.list_all_table_composer import list_all_table_composer
from src.composer.restaurant_table.delete_table_composer import delete_table_composer
from src.composer.restaurant_table_presenter_composer import restaurant_table_presenter_composer
from src.schemas.restaurant_table_schemas.restaurant_table_schemas import CreateRestaurantTableSchema


bp = Blueprint('restaurant_table', __name__, url_prefix='/tables')

@bp.route('/', methods=["POST"])
def create_restaurant_table():
    try:
        data = request.json
        schema = CreateRestaurantTableSchema()
        validated_data = schema.load(data)
        
        use_case = create_table_composer()
        response = use_case.create_restaurant_table(validated_data)
        
        presenter = restaurant_table_presenter_composer()
        formatted_response = presenter.format_table_presenter(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise

@bp.route('/<int:table_number>', methods=["GET"])
def list_restaurant_table_by_number(table_number):
    try:
        use_case = list_table_composer()
        response = use_case.list_table_by_number(table_number)
        
        presenter = restaurant_table_presenter_composer()
        formatted_response = presenter.format_table_presenter(response)
        return formatted_response, HTTPStatus.OK
    except Exception as exc:
        raise

@bp.route('/', methods=["GET"])
def list_all_restaurant_table():
    try:
        use_case = list_all_table_composer()
        response = use_case.list_all_table()
        
        presenter = restaurant_table_presenter_composer()
        formatted_response = presenter.format_all_table_presenter(response)
        return formatted_response, HTTPStatus.OK
    except Exception as exc:
        raise

@bp.route('/<int:table_number', methods=["DELETE"])
def delete_restaurant_table(table_number):
    try:
        use_case = delete_table_composer()
        response = use_case.delete_table(table_number)
        
        return None, HTTPStatus.NO_CONTENT
    except Exception as exc:
        raise