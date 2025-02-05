from src.models.orders import Orders
from src.models.restaurant_table import RestaurantTable
from src.repositories.orders.orders_repository import OrdersRepository

def test_orders_repository_create_order(db_session):
    restaurant_table = RestaurantTable(table_number = 125)
    db_session.add(restaurant_table)
    db_session.commit()
    
    restaurant_table_on_db = db_session.query(RestaurantTable).filter_by(table_number=restaurant_table.table_number).first()
    
    repository = OrdersRepository()
    data = {"restaurant_table_id": restaurant_table_on_db.id}
    
    result = repository.create_order(data)
    
    assert result.restaurant_table_id == restaurant_table_on_db.id
    assert result.order_status == "Em preparo"
    
    db_session.delete(restaurant_table_on_db)
    db_session.commit()
    
    db_session.delete(result)
    db_session.commit()  