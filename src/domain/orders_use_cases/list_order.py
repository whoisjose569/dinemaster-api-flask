from src.repositories.orders.orders_repository import OrdersRepository
from src.errors.custom_errors import NotOrdersAvailable

class ListOrderService:
    def __init__(self, orders_repository: OrdersRepository):
        self.__orders_repository = orders_repository
    
    def list_order(self, order_id):
        order_on_db = self.__orders_repository.check_order_exists(order_id)
        if not order_on_db:
            raise NotOrdersAvailable()
        return order_on_db
        