import pytest
from marshmallow.exceptions import ValidationError
from src.schemas.order_schemas.order_schemas import UpdateOrderSchema, CreateOrderSchema
from src.errors.custom_errors import OrderStatusMustBeAString, OrderQuantityMustBeAInteger, OrderQuantityMustBeAGreaterThanZero, OrderPriceMustBeAFloat

@pytest.fixture
def schema():
    return CreateOrderSchema()

def test_valid_order_schema(schema):
    data = {
    "restaurant_table_id": 1,
    "order_items": [
    {"item": "X-Bacon", "quantity": 1, "price": 12.50},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
        ]
    }
    valid_data = schema.load(data)
    
    assert valid_data["restaurant_table_id"] == 1
    assert valid_data["order_items"] == [
    {"item": "X-Bacon", "quantity": 1, "price": 12.50},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
    ]
    assert valid_data["order_status"] == "Em preparo"
    assert valid_data["delivery_type"] == "Local"

def test_invalid_order_status(schema):
    data = {
    "restaurant_table_id": 1,
    "order_status": 10,
    "order_items": [
    {"item": "X-Bacon", "quantity": 1, "price": 12.50},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
        ]
    }
    with pytest.raises(OrderStatusMustBeAString) as exc_info:
        schema.load(data)
    assert 'Order status must be an string' in str(exc_info)

def test_invalid_order_quantity(schema):
    data = {
    "restaurant_table_id": 1,
    "order_items": [
    {"item": "X-Bacon", "quantity": "1", "price": 12.50},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
        ]
    }
    with pytest.raises(OrderQuantityMustBeAInteger):
        schema.load(data)

def test_order_quantity_less_than_zero(schema):
    data = {
    "restaurant_table_id": 1,
    "order_items": [
    {"item": "X-Bacon", "quantity": 0, "price": 12.50},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
        ]
    }
    with pytest.raises(OrderQuantityMustBeAGreaterThanZero):
        schema.load(data)

def test_order_price_must_be_a_float(schema):
    data = {
    "restaurant_table_id": 1,
    "order_items": [
    {"item": "X-Bacon", "quantity": 0, "price": 12},
    {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
        ]
    }
    with pytest.raises(OrderPriceMustBeAFloat):
        schema.load(data)
