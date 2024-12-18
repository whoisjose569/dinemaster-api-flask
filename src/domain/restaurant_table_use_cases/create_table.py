from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.errors.custom_errors import TableAlreadyExistsError

class CreateRestaurantTableService:
    def __init__(self, restaurant_table_repository: RestaurantTableRepository):
        self.__restaurant_table_repository = restaurant_table_repository
    
    def create_restaurant_table(self, data):
        if self.__restaurant_table_repository.check_table_number_exists(data):
            raise TableAlreadyExistsError(data["table_number"])
        return self.__restaurant_table_repository.create_restaurant_table(data)
        