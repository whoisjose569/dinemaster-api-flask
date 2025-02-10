from src.repositories.orders.orders_repository import OrdersRepository
from src.domain.orders_use_cases.list_order import ListOrderService

def list_order_composer():
    repo = OrdersRepository()
    service = ListOrderService(repo)
    
    return service
    