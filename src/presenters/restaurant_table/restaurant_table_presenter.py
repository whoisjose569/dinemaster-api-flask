class RestaurantTablePresenter:
    def format_table_presenter(self, data):
        return{
            "msg": 'RestaurantTable created!.',
            "id": data.id,
            "table_number": data.table_number,
            "table_status": data.table_status
        }
    