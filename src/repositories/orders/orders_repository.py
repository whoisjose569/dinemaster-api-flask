from src.models.restaurant_table import RestaurantTable
from src.models.orders import Orders
from src.models.base import db

class OrdersRepository:
    def __init__(self):
        self.__session = db.session

    def check_table_exists(self, data):
        return self.__session.query(RestaurantTable).filter_by(id = data["restaurant_table_id"]).first()
    
    def create_order(self, data):
        new_order = Orders(**data)
        self.__session.add(new_order)
        self.__session.commit()
        return new_order