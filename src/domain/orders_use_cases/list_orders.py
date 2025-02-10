from src.repositories.orders.orders_repository import OrdersRepository
from src.errors.custom_errors import NotOrdersAvailable

class ListOrdersService:
    def __init__(self, orders_repository: OrdersRepository):
        self.orders_repository = orders_repository
    
    def list_orders(self):
        orders_on_db = self.orders_repository.list_orders()
        if not orders_on_db:
            raise NotOrdersAvailable()
        return orders_on_db