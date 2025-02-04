import json
class OrderPresenter:
    def format_order_presenter(self, data):
        return{
            "id": data.id,
            "restaurant_table_id": data.restaurant_table_id,
            "create_at": data.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            "order_status": data.order_status,
            "delivery_type": data.delivery_type,
            "order_items": [
                {"item": item["item"], "quantity": item["quantity"], "price": item["price"]}
                for item in json.loads(data.order_items)  
            ] if data.order_items else [] 
        }