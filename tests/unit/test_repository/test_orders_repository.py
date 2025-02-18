import json
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

def test_orders_repository_list_orders(db_session):
    restaurant_table = RestaurantTable(table_number = 125)
    db_session.add(restaurant_table)
    db_session.commit()

    restaurant_table_on_db = db_session.query(RestaurantTable).filter_by(table_number=restaurant_table.table_number).first() 
    
    items = [
        {"item": "X-Bacon", "quantity": 1, "price": 12.50},
        {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
    ]
    
    order = Orders(restaurant_table_id = restaurant_table_on_db.id, order_items = json.dumps(items))
    db_session.add(order)
    db_session.commit()
    
    repo = OrdersRepository()
    
    order_on_db = repo.list_orders()
    order_on_db_items = json.loads(order_on_db[0].order_items)
    
    assert order_on_db[0].restaurant_table_id == restaurant_table_on_db.id
    assert order_on_db_items == items
    
    db_session.delete(order_on_db[0])
    db_session.commit()
    
    db_session.delete(restaurant_table_on_db)
    db_session.commit()

def test_orders_repository_list_order(db_session):
    restaurant_table = RestaurantTable(table_number = 125)
    db_session.add(restaurant_table)
    db_session.commit()

    restaurant_table_on_db = db_session.query(RestaurantTable).filter_by(table_number=restaurant_table.table_number).first() 
    
    items = [
        {"item": "X-Bacon", "quantity": 1, "price": 12.50},
        {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
    ]
    
    order = Orders(restaurant_table_id = restaurant_table_on_db.id, order_items = json.dumps(items))
    db_session.add(order)
    db_session.commit()
    
    repo = OrdersRepository()
    
    order_on_db = repo.list_order(order.id)
    order_on_db_items = json.loads(order_on_db.order_items)
    
    assert order_on_db.restaurant_table_id == restaurant_table_on_db.id
    assert order_on_db_items == items
    
    db_session.delete(order_on_db)
    db_session.commit()
    
    db_session.delete(restaurant_table_on_db)
    db_session.commit()

def test_orders_repository_update_order(db_session):
    restaurant_table = RestaurantTable(table_number = 125)
    db_session.add(restaurant_table)
    db_session.commit()

    restaurant_table_on_db = db_session.query(RestaurantTable).filter_by(table_number=restaurant_table.table_number).first() 
    
    items = [
        {"item": "X-Bacon", "quantity": 1, "price": 12.50},
        {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
    ]
    
    order = Orders(restaurant_table_id = restaurant_table_on_db.id, order_items = json.dumps(items))
    db_session.add(order)
    db_session.commit()
    
    repo = OrdersRepository()
    
    order_status = {"order_status": "Retirada"}
    
    result = repo.update_order(restaurant_table_on_db.id, order_status)
    
    order_on_db = db_session.query(Orders).filter_by(id=order.id).first()
    
    assert order_on_db.order_status == result.order_status
    
    db_session.delete(restaurant_table_on_db)
    db_session.commit()
    
    db_session.delete(order_on_db)
    db_session.commit()

def test_orders_delete_order(db_session):
    restaurant_table = RestaurantTable(table_number = 125)
    db_session.add(restaurant_table)
    db_session.commit()

    restaurant_table_on_db = db_session.query(RestaurantTable).filter_by(table_number=restaurant_table.table_number).first() 
    
    items = [
        {"item": "X-Bacon", "quantity": 1, "price": 12.50},
        {"item": "Coca-Cola Lata", "quantity": 2, "price": 5.00}
    ]
    
    order = Orders(restaurant_table_id = restaurant_table_on_db.id, order_items = json.dumps(items))
    db_session.add(order)
    db_session.commit()
    
    repo = OrdersRepository()
    
    result = repo.delete_order(order.id)
    
    assert result is None
    
    db_session.delete(restaurant_table_on_db)
    db_session.commit()