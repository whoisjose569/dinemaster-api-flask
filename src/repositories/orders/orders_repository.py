from src.models.orders import Orders
from src.models.base import db

class OrdersRepository:
    def __init__(self):
        self.__session = db.session
    
    def create_order(self, data):
        new_order = Orders(**data)
        self.__session.add(new_order)
        self.__session.commit()
        return new_order