import pytest
from marshmallow.exceptions import ValidationError
from src.schemas.restaurant_table_schemas.restaurant_table_schemas import CreateRestaurantTableSchema
from src.errors.custom_errors import TableNumberValidationError, TableNumberMustBeANumber

@pytest.fixture
def schema():
    return CreateRestaurantTableSchema()

def test_valid_table_number(schema):
    data = {"table_number": 1}
    valid_data = schema.load(data)
    assert valid_data["table_number"] == 1

def test_table_number_is_negative(schema):
    data = {"table_number": -1}
    with pytest.raises(TableNumberValidationError) as exc_info:
        schema.load(data) 
    assert "Table number must be positive" in str(exc_info)

def test_table_number_is_not_a_number(schema):
    data = {"table_number": "a"}
    with pytest.raises(TableNumberMustBeANumber) as exc_info:
        schema.load(data) 
    assert "Table number must be an integer" in str(exc_info)

def test_missing_table_number(schema):
    data = {}
    with pytest.raises(ValidationError) as exc_info:
        schema.load(data)
    assert "Missing data for required field." in str(exc_info)
        
    