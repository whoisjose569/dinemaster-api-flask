from marshmallow import fields, validates
from src.models.restaurant_table import RestaurantTable
from src.errors.custom_errors import TableNumberValidationError, TableNumberMustBeANumber, TableStatusMustBeAString
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

class UpdateRestaurantTableSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantTable
        exclude = ("id", "table_number",)
    
    table_status = fields.Raw(required=True)
    
    @validates("table_status")
    def validate_table_status(self, value):
        if not isinstance(value, str):
            raise TableStatusMustBeAString("Table number must be an String")
    
    
    