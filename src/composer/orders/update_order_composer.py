from src.repositories.orders.orders_repository import OrdersRepository
from src.domain.orders_use_cases.update_order import UpdateOrderStatusService

def update_order_composer():
    repo = OrdersRepository()
    service = UpdateOrderStatusService(repo)
    return service