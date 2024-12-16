def format_table_presenter(table):
    return {'RestaurantTable': {
        "id": table.id,
        "table_number": table.table_number,
        "table_status": table.table_status
    }}
    