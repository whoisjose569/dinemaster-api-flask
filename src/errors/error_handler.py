from flask import json
from werkzeug.exceptions import HTTPException
from src.errors.custom_errors import *

def register_error_handlers(app):

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.errorhandler(TableAlreadyExistsError)
    def handle_table_already_exists_error(e):
        return {
            "code": 409,
            "name": "Conflict",
            "description": str(e),
        }, 409

    @app.errorhandler(TableNumberValidationError)
    def handle_table_number_validation_error(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(OrderQuantityMustBeAInteger)
    def handle_order_item_quantity(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(OrderQuantityMustBeAGreaterThanZero)
    def handle_order_item_quantity_greater_than_zero(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(OrderPriceMustBeAFloat)
    def handle_order_item_price_must_be_a_float(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(TableNumberMustBeANumber)
    def handle_table_number_validation_error(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(TableNotExists)
    def handle_table_not_exists(e):
        return {
            "code": 404,
            "name": "NotFound",
            "description": str(e),
        }, 404

    @app.errorhandler(NotTablesAvailable)
    def handle_not_tables_available(e):
        return {
            "code": 404,
            "name": "NotFound",
            "description": str(e),
        }, 404

    @app.errorhandler(TableStatusMustBeAString)
    def handle_table_status_validation_error(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(OrderStatusMustBeAString)
    def handle_order_status_validation_error(e):
        return {
            "code": 400,
            "name": "Bad Request",
            "description": str(e),
        }, 400

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return {
            "code": 500,
            "name": "Internal Server Error",
            "description": "Something Went Wrong on the Server.",
        }, 500