from src.models.restaurant_table import RestaurantTable
from src.models.base import db

def _check_table_number_exists(data):
    return db.session.query(RestaurantTable).filter_by(table_number = data["table_number"]).first()

def _create_restaurant_table(data):
    restaurant_table = RestaurantTable(table_number=data['table_number'])
    db.session.add(restaurant_table)
    db.session.commit()
    return restaurant_table

    