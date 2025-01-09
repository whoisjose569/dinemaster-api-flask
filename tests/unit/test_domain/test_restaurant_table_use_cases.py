import pytest
from src.domain.restaurant_table_use_cases.create_table import CreateRestaurantTableService
from src.domain.restaurant_table_use_cases.list_table import ListRestaurantTableService
from src.errors.custom_errors import TableAlreadyExistsError, TableNotExists


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
    