from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.errors.custom_errors import TableNotExists

class UpdateRestaurantTableService:
    def __init__(self, restaurant_table_repository: RestaurantTableRepository):
        self.__restaurant_table_repository = restaurant_table_repository
    
    def update_table(self, table_number, data):
        if not self.__restaurant_table_repository.check_table_exists(table_number):
            raise TableNotExists(table_number)
        return self.__restaurant_table_repository.update_restaurant_table(table_number, data)