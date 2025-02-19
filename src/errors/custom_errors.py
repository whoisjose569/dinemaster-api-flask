class RestaurantTableError(Exception):
    pass

class OrderError(Exception):
    pass

class UsersError(Exception):
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

class OrderStatusMustBeAString(OrderError):
    def __init__(self, table_number):
        super().__init__(f'Order status must be an string')

class OrderQuantityMustBeAInteger(OrderError):
    def __init__(self, table_number):
        super().__init__(f'Order quantity must be an integer')

class OrderQuantityMustBeAGreaterThanZero(OrderError):
    def __init__(self, table_number):
        super().__init__(f'Quantity must be greater than zero')

class OrderPriceMustBeAFloat(OrderError):
    def __init__(self, table_number):
        super().__init__(f'Price must be a float')

class NotOrdersAvailable(OrderError):
    def __init__(self):
        super().__init__(f'No orders available to list.')

class UserNotFound(UsersError):
    def __init__(self):
        super().__init__(f'User not found.')

class UserWrongPassword(UsersError):
    def __init__(self):
        super().__init__(f'User wrong password')