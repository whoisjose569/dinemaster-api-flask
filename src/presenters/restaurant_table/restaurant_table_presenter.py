class RestaurantTablePresenter:
    def format_table_presenter(self, data):
        return{
            "id": data.id,
            "table_number": data.table_number,
            "table_status": data.table_status
        }
    
    def format_all_table_presenter(self, data):
        return [{
            "id": table.id,
            "table_number": table.table_number,
            "table_status": table.table_status
        } for table in data]
    