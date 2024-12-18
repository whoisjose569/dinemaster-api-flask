from src.repositories.restaurant_table.restaurant_table_repository import RestaurantTableRepository
from src.domain.restaurant_table_use_cases.create_table import CreateRestaurantTableService

def create_table_composer():
    repo = RestaurantTableRepository()
    service = CreateRestaurantTableService(repo)
    return service
    