from src.models.orders import Orders
from src.models.restaurant_table import RestaurantTable

def test_orders_model_default():
    restaurant_table = RestaurantTable(table_number = 125)

    order = Orders(restaurant_table_id = restaurant_table.id)

    assert order.restaurant_table_id == restaurant_table.id

def test_orders_model_custom_order_status():
    restaurant_table = RestaurantTable(table_number = 125)

    order = Orders(restaurant_table_id = restaurant_table.id, order_status= "Em preparo")

    assert order.restaurant_table_id == restaurant_table.id
    assert order.order_status == "Em preparo"

def test_orders_model_delivery_type():
    order = Orders(delivery_type="Entrega")
    
    assert order.delivery_type == "Entrega"

def test_orders_model_default():
    order = Orders()
    
    assert order is not None