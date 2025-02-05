import pytest
from src.domain.orders_use_cases.create_order import CreateOrderService
from src.errors.custom_errors import TableNotExists

def test_create_order_when_table_not_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_exists.return_value = False
    service = CreateOrderService(mock_repo)
    
    data = {"restaurant_table_id": 999}
    
    with pytest.raises(TableNotExists):
        service.create_order(data)
    
    mock_repo.check_table_exists.assert_called_once_with(data)