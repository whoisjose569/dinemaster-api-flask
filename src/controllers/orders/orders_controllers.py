from flask import Blueprint, request
from http import HTTPStatus
from src.composer.orders_presenter_composer import order_presenter_composer
from src.composer.orders.create_order_composer import create_order_composer

bp = Blueprint('orders',__name__,url_prefix="/orders")

@bp.route('/',methods=["POST"])
def create_order():
    try:
        data = request.json
        use_case = create_order_composer()
        response = use_case.create_order(data)

        presenter = order_presenter_composer()
        formatted_response = presenter.format_order_presenter(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise
        
        
        