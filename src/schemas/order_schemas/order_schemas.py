from marshmallow import fields, validates
from src.models.orders import Orders
from src.errors.custom_errors import OrderStatusMustBeAString, OrderQuantityMustBeAInteger, OrderQuantityMustBeAGreaterThanZero, OrderPriceMustBeAFloat
from src.utils import ma

class OrderItemSchema(ma.Schema):
    item = fields.Raw(required=True)
    quantity = fields.Raw(required=True)
    price = fields.Raw(required=True)
    
    @validates("quantity")
    def validate_quantity(self, value):
        if not isinstance(value, int):
            raise OrderQuantityMustBeAInteger("Order quantity must be an Integer")
    
    @validates("quantity")
    def validate_quantity_greater_than_zero(self, value):
        if value <= 0:
            raise OrderQuantityMustBeAGreaterThanZero("Quantity must be greater than zero")

    @validates("price")
    def validate_price_must_be_a_float(self, value):
        if not isinstance(value, float):
            raise OrderPriceMustBeAFloat("Price must be a Float")
        
class CreateOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders
        exclude = ("id",)
    
    restaurant_table_id = fields.Integer(load_default=None)
    order_status = fields.Raw(load_default="Em preparo")
    delivery_type = fields.String(load_default=None)
    order_items = fields.List(fields.Nested(OrderItemSchema), load_default=[])
    
    @validates("order_status")
    def validate_order_status(self, value):
        if not isinstance(value, str):
            raise OrderStatusMustBeAString("Order status must be an String")