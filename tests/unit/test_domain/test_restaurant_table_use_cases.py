import pytest
from src.domain.restaurant_table_use_cases.create_table import CreateRestaurantTableService
from src.domain.restaurant_table_use_cases.list_table import ListRestaurantTableService
from src.domain.restaurant_table_use_cases.list_all_tables import ListAllRestaurantTableService
from src.domain.restaurant_table_use_cases.delete_table import DeleteRestaurantTableService
from src.domain.restaurant_table_use_cases.update_table import UpdateRestaurantTableService
from src.errors.custom_errors import TableAlreadyExistsError, TableNotExists, NotTablesAvailable


def test_create_restaurant_table_raises_error_when_table_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_number_exists.return_value = True
    service = CreateRestaurantTableService(mock_repo)
    
    with pytest.raises(TableAlreadyExistsError):
        service.create_restaurant_table({"table_number": 1})
    
    mock_repo.check_table_number_exists.assert_called_once_with({"table_number": 1})

def test_create_restaurant_table_when_table_not_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_number_exists.return_value = False
    service = CreateRestaurantTableService(mock_repo)
    
    data = {"table_number": 1}
    
    service.create_restaurant_table(data)
    
    mock_repo.create_restaurant_table.assert_called_once_with(data)
    mock_repo.check_table_number_exists.assert_called_once_with(data)

def test_list_restaurant_table_raises_table_not_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.list_restaurant_table_by_number.return_value = None
    
    service = ListRestaurantTableService(mock_repo)
    
    with pytest.raises(TableNotExists):
        service.list_table_by_number(1)

def test_list_restaurant_table_raises_not_tables_available(mocker):
    mock_repo = mocker.Mock()
    mock_repo.list_restaurant_table.return_value = None
    
    service = ListAllRestaurantTableService(mock_repo)
    
    with pytest.raises(NotTablesAvailable):
        service.list_all_table()

def test_delete_restaurant_table_raises_error_when_table_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_exists.return_value = False
    service = DeleteRestaurantTableService(mock_repo)
    
    with pytest.raises(TableNotExists):
        service.delete_table(1)

def test_update_restaurant_table_raises_table_not_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_exists.return_value = None
    
    service = UpdateRestaurantTableService(mock_repo)
    
    with pytest.raises(TableNotExists):
        service.update_table(21, {"table_status": "ocupado"})