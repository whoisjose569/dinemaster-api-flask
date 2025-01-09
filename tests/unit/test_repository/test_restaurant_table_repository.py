from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.models.restaurant_table import RestaurantTable

def test_check_table_number_exists(db_session):
    existing_table = RestaurantTable(table_number = 1)
    db_session.add(existing_table)
    db_session.commit()
    
    repository = RestaurantTableRepository()
    
    result = repository.check_table_number_exists({"table_number": 1})
    
    assert result is not None
    assert result.table_number == 1
    
    db_session.delete(existing_table)
    db_session.commit()

def test_list_table_by_number(db_session):
    existing_table = RestaurantTable(table_number = 1)
    db_session.add(existing_table)
    db_session.commit()
    
    repository = RestaurantTableRepository()
    
    result = repository.list_restaurant_table_by_number(1)
    
    assert result is not None
    assert result.table_number == 1
    
    db_session.delete(existing_table)
    db_session.commit()