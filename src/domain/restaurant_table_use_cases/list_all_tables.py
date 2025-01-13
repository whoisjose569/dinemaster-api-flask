from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.errors.custom_errors import NotTablesAvailable

class ListAllRestaurantTableService:
    def __init__(self, restaurant_table_repository: RestaurantTableRepository):
        self.__restaurant_table_repository = restaurant_table_repository
    
    def list_all_table(self):
        if not self.__restaurant_table_repository.list_restaurant_table():
            raise NotTablesAvailable()
        return self.__restaurant_table_repository.list_restaurant_table()