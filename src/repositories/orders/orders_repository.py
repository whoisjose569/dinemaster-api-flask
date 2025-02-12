from src.models.restaurant_table import RestaurantTable
from src.models.orders import Orders
from src.models.base import db
import json

class OrdersRepository:
    def __init__(self):
        self.__session = db.session

    def check_table_exists(self, data):
        return self.__session.query(RestaurantTable).filter_by(id = data["restaurant_table_id"]).first()
    
    def check_order_exists(self, order_id):
        return self.__session.query(Orders).filter_by(id = order_id).first()
    
    def create_order(self, data):
        if "order_items" in data:
            data["order_items"] = json.dumps(data["order_items"])
        new_order = Orders(**data)
        self.__session.add(new_order)
        self.__session.commit()
        return new_order
    
    def list_orders(self):
        orders_on_db = self.__session.query(Orders).all()
        return orders_on_db
    
    def list_order(self, order_id):
        order_on_db = self.__session.query(Orders).filter_by(id = order_id).first()
        return order_on_db

    def update_order(self, order_id, data):
        order_on_db = self.__session.query(Orders).filter_by(id=order_id).first()
        order_on_db.order_status = data["order_status"]
        self.__session.commit()
        return order_on_db
        
        