from src.repositories.orders.orders_repository import OrdersRepository
from src.errors.custom_errors import TableNotExists

class CreateOrderService:
    def __init__(self, orders_repository: OrdersRepository):
        self.__orders_repository = orders_repository
    
    def create_order(self, data):
        if data["restaurant_table_id"] is not None:
            if not self.__orders_repository.check_table_exists(data):
                raise TableNotExists(data['restaurant_table_id'])      
        return self.__orders_repository.create_order(data)
    