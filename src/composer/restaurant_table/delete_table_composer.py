from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.domain.restaurant_table_use_cases.delete_table import DeleteRestaurantTableService

def delete_table_composer():
    repo = RestaurantTableRepository()
    service = DeleteRestaurantTableService(repo)
    return service
    