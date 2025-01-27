from src.repositories.orders.orders_repository import OrdersRepository

class CreateOrderService:
    def __init__(self, orders_repository: OrdersRepository):
        self.__orders_repository = orders_repository
    
    def create_order(self, data):
        return self.__orders_repository.create_order(data)
    