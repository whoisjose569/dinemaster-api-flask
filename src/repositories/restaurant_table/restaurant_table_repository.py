from src.models.restaurant_table import RestaurantTable
from src.models.base import db
from src.errors.custom_errors import TableAlreadyExistsError

class RestaurantTableRepository:
    def __init__(self):
        self.__session = db.session
    
    def check_table_number_exists(self, data):
        return self.__session.query(RestaurantTable).filter_by(table_number = data["table_number"]).first()

    def create_restaurant_table(self, data):
        restaurant_table = RestaurantTable(table_number=data['table_number'])
        self.__session.add(restaurant_table)
        self.__session.commit()
        return restaurant_table