class RestaurantTableError(Exception):
    pass

class TableAlreadyExistsError(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'The table with the number {table_number} is already registered.')