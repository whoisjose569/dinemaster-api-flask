from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.errors.custom_errors import TableNotExists


class DeleteRestaurantTableService:
    def __init__(self, restaurant_table_repository = RestaurantTableRepository):
        self.__restaurant_table_repository = restaurant_table_repository
    
    def delete_table(self, table_number):
        if not self.__restaurant_table_repository.check_table_number_exists(table_number):
            raise TableNotExists(table_number)
        return self.__restaurant_table_repository.delete_restaurant_table(table_number)