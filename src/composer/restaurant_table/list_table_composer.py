from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.domain.restaurant_table_use_cases.list_table import ListRestaurantTableService

def list_table_composer():
    repo = RestaurantTableRepository()
    service = ListRestaurantTableService(repo)
    return service