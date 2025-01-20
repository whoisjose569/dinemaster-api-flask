from src.domain.restaurant_table_use_cases.update_table import UpdateRestaurantTableService
from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository

def update_table_composer():
    repo = RestaurantTableRepository()
    service  = UpdateRestaurantTableService(repo)
    return service