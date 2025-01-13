from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.domain.restaurant_table_use_cases.list_all_tables import ListAllRestaurantTableService

def list_all_table_composer():
    repo = RestaurantTableRepository()
    service = ListAllRestaurantTableService(repo)
    return service