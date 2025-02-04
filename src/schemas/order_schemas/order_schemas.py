from marshmallow import fields, validates
from src.models.orders import Orders
from src.errors.custom_errors import OrderStatusMustBeAString
from src.utils import ma

class CreateOrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Orders
        exclude = ("id",)
    
    restaurant_table_id = fields.Integer(load_default=None)
    order_status = fields.Raw(load_default="Em preparo")
    delivery_type = fields.String(load_default=None)
    order_items = fields.List(fields.Dict(), load_default=[])
    
    @validates("order_status")
    def validate_order_status(self, value):
        if not isinstance(value, str):
            raise OrderStatusMustBeAString("Order status must be an String")