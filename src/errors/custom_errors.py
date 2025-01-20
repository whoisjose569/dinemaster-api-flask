class RestaurantTableError(Exception):
    pass

class TableAlreadyExistsError(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'The table with the number {table_number} is already registered.')

class TableNumberValidationError(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'Table number must be positive')
class TableNumberMustBeANumber(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'Table number must be an integer')

class TableNotExists(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'The table with the number {table_number} not exists.')
    
class NotTablesAvailable(RestaurantTableError):
    def __init__(self):
        super().__init__(f'No tables available to list.')

class TableStatusMustBeAString(RestaurantTableError):
    def __init__(self, table_number):
        super().__init__(f'Table status must be an string')