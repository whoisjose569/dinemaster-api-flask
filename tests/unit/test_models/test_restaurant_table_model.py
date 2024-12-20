import pytest
from src.models.restaurant_table import RestaurantTable

def test_restaurant_table_defaults():
    table = RestaurantTable(table_number=1)
    assert table.table_status is None
    assert table.table_number == 1

def test_restaurant_table_custom_status():
    table = RestaurantTable(table_number=1, table_status="ocupado")
    assert table.table_status == "ocupado"