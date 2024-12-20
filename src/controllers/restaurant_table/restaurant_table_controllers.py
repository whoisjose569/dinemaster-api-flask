from flask import Blueprint, request
from http import HTTPStatus
from src.composer.restaurant_table.create_table_composer import create_table_composer
from src.composer.restaurant_table_presenter_composer import create_restaurant_table_presenter_composer
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
        
        presenter = create_restaurant_table_presenter_composer()
        formatted_response = presenter.format_table_presenter(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise