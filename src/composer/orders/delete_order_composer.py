from src.repositories.orders.orders_repository import OrdersRepository
from src.domain.orders_use_cases.delete_order import DeleteOrderService

def delete_order_composer():
    repo = OrdersRepository()
    service = DeleteOrderService(repo)
    return service