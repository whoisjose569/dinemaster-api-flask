from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.errors.custom_errors import TableNotExists

class ListRestaurantTableService:
    def __init__(self, restaurant_table_repository: RestaurantTableRepository):
        self.__restaurant_table_repository = restaurant_table_repository
    
    def list_table_by_number(self, table_number):
        if not self.__restaurant_table_repository.list_restaurant_table_by_number(table_number):
            raise TableNotExists(table_number)
        return self.__restaurant_table_repository.list_restaurant_table_by_number(table_number)
            
    
