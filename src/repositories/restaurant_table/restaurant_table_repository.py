from src.models.restaurant_table import RestaurantTable
from src.models.base import db

class RestaurantTableRepository:
    def __init__(self):
        self.__session = db.session
    
    def check_table_number_exists(self, data):
        return self.__session.query(RestaurantTable).filter_by(table_number = data["table_number"]).first()
    
    def check_table_exists(self, table_number):
        return self.__session.query(RestaurantTable).filter_by(table_number = table_number).first()

    def create_restaurant_table(self, data):
        restaurant_table = RestaurantTable(table_number=data['table_number'])
        self.__session.add(restaurant_table)
        self.__session.commit()
        return restaurant_table
    
    def list_restaurant_table_by_number(self, table_number):
        restaraunt_table = self.__session.query(RestaurantTable).filter_by(table_number=table_number).first()
        return restaraunt_table
    
    def list_restaurant_table(self):
        restaurant_table = self.__session.query(RestaurantTable).all()
        return restaurant_table
    
    def delete_restaurant_table(self, table_number):
        restaurant_table = self.__session.query(RestaurantTable).filter_by(table_number=table_number).first()
        self.__session.delete(restaurant_table)
        self.__session.commit()
        return restaurant_table