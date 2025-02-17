import pytest
from src.domain.orders_use_cases.create_order import CreateOrderService
from src.domain.orders_use_cases.list_orders import ListOrdersService
from src.domain.orders_use_cases.list_order import ListOrderService
from src.domain.orders_use_cases.update_order import UpdateOrderStatusService
from src.errors.custom_errors import TableNotExists, NotOrdersAvailable

def test_create_order_when_table_not_exists(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_table_exists.return_value = False
    service = CreateOrderService(mock_repo)
    
    data = {"restaurant_table_id": 999}
    
    with pytest.raises(TableNotExists):
        service.create_order(data)
    
    mock_repo.check_table_exists.assert_called_once_with(data)

def test_list_orders_not_orders_available(mocker):
    mock_repo = mocker.Mock()
    mock_repo.list_orders.return_value = False
    
    service = ListOrdersService(mock_repo)
    
    with pytest.raises(NotOrdersAvailable):
        service.list_orders()

def test_list_orders_not_order_available(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_order_exists.return_value = None
    
    service = ListOrderService(mock_repo)
    
    with pytest.raises(NotOrdersAvailable):
        service.list_order(1)

def test_update_order_not_order_available(mocker):
    mock_repo = mocker.Mock()
    mock_repo.check_order_exists.return_value = None
    
    service = UpdateOrderStatusService(mock_repo)
    data = {}
    
    with pytest.raises(NotOrdersAvailable):
        service.update_order(1, data)