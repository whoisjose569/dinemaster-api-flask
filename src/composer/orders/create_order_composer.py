from src.repositories.orders.orders_repository import OrdersRepository
from src.domain.orders_use_cases.create_order import CreateOrderService

def create_order_composer():
    repo = OrdersRepository()
    service = CreateOrderService(repo)
    return service
    