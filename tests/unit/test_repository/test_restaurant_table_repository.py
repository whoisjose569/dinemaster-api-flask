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

def test_list_all_tables(db_session):
    existing_table_one = RestaurantTable(table_number = 1)
    db_session.add(existing_table_one)
    db_session.commit()
    
    existing_table_two = RestaurantTable(table_number = 2)
    db_session.add(existing_table_two)
    db_session.commit()
    
    repository = RestaurantTableRepository()
    
    result = repository.list_restaurant_table()
    
    assert result is not None
    assert len(result) == 2
    assert result[0].id == existing_table_one.id
    assert result[0].table_number == existing_table_one.table_number
    assert result[0].table_status == existing_table_one.table_status
    assert result[1].id == existing_table_two.id
    assert result[1].table_number == existing_table_two.table_number
    assert result[1].table_status == existing_table_two.table_status
    
    db_session.delete(existing_table_one)
    db_session.commit()
    
    db_session.delete(existing_table_two)
    db_session.commit()

def test_delete_table(db_session):
    new_table = RestaurantTable(table_number = 1)
    db_session.add(new_table)
    db_session.commit()
    
    repository = RestaurantTableRepository()
    result = repository.delete_restaurant_table(1)
    
    assert result is None