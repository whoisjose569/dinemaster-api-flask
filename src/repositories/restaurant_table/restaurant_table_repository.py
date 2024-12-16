from src.models.restaurant_table import RestaurantTable
from src.models.base import db
from src.errors.custom_errors import TableAlreadyExistsError

def _check_table_number_exists(data):
    table_on_db = db.session.query(RestaurantTable).filter_by(table_number = data["table_number"]).first()
    if table_on_db:
        raise TableAlreadyExistsError(data["table_number"])

def _create_restaurant_table(data):
    restaurant_table = RestaurantTable(table_number=data['table_number'])
    db.session.add(restaurant_table)
    db.session.commit()
    return restaurant_table

    