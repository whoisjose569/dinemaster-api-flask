from marshmallow import fields, validates
from src.models.restaurant_table import RestaurantTable
from src.errors.custom_errors import TableNumberValidationError, TableNumberMustBeANumber
from src.utils import ma

class CreateRestaurantTableSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantTable
        exclude = ("id",)
    
    table_status = fields.String(load_default=None)
    table_number = fields.Raw(required=True)
    
    @validates("table_number")
    def validate_table_number(self, value):
        if not isinstance(value, int):
            raise TableNumberMustBeANumber("Table number must be an integer")
        if value <= 0:
            raise TableNumberValidationError("Table number must be positive")
    
    
    