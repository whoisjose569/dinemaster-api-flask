from src.repositories.orders.orders_repository import OrdersRepository
from src.domain.orders_use_cases.list_orders import ListOrdersService

def list_orders_composer():
    repo = OrdersRepository()
    service = ListOrdersService(repo)
    
    return service