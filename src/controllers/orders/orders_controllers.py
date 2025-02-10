from flask import Blueprint, request
from http import HTTPStatus
from src.schemas.order_schemas.order_schemas import CreateOrderSchema
from src.composer.orders_presenter_composer import order_presenter_composer
from src.composer.orders.create_order_composer import create_order_composer
from src.composer.orders.list_orders_composer import list_orders_composer

bp = Blueprint('orders',__name__,url_prefix="/orders")

@bp.route('/',methods=["POST"])
def create_order():
    try:
        data = request.json
        schema = CreateOrderSchema()
        
        validated_data = schema.load(data)
        
        use_case = create_order_composer()
        response = use_case.create_order(validated_data)

        presenter = order_presenter_composer()
        formatted_response = presenter.format_order_presenter(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise

@bp.route('/',methods=["GET"])
def list_oders():
    try:
        use_case = list_orders_composer()
        response = use_case.list_orders()

        presenter = order_presenter_composer()
        formatted_response = presenter.format_all_orders_presenter(response)
        return formatted_response, HTTPStatus.OK
    except Exception as exc:
        raise         
        
        