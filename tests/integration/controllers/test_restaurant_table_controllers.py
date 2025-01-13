from http import HTTPStatus
from src.controllers.restaurant_table.restaurant_table_controllers import bp
from src.models.restaurant_table import RestaurantTable


def test_create_table(client, mocker, db_session):
    mock_create_table_composer = mocker.patch('src.composer.restaurant_table.create_table_composer')
    mock_service = mocker.Mock()
    mock_create_table_composer.return_value = mock_service

    mock_presenter_composer = mocker.patch('src.composer.restaurant_table_presenter_composer')
    mock_presenter = mocker.Mock()
    mock_presenter_composer.return_value = mock_presenter
    
    data = {"table_number": 1}

    mock_service.create_restaurant_table.return_value = {"table_number": 1}

    mock_presenter.format_table_presenter.return_value = {"table_number": 1}
    
    response = client.post('/tables/', json=data)
 
    assert response.status_code == HTTPStatus.CREATED
    
    assert response.json == {
            "id": 1,
            "table_number": 1,
            "table_status": "livre"
        }

    table_in_db = db_session.query(RestaurantTable).filter_by(table_number=1).first()
    db_session.delete(table_in_db)
    db_session.commit()
    
def test_list_table_by_number(client, mocker, db_session):
    mock_list_table_composer = mocker.patch('src.composer.restaurant_table.list_table_composer')
    mock_service = mocker.Mock()
    mock_list_table_composer.return_value = mock_service
    
    mock_presenter_composer = mocker.patch('src.composer.restaurant_table_presenter_composer')
    mock_presenter = mocker.Mock()
    mock_presenter_composer.return_value = mock_presenter
    
    table = RestaurantTable(table_number = 1)
    db_session.add(table)
    db_session.commit()
    
    data = {"id": 1, "table_number": 1, "table_status": "livre"}
    
    mock_service.list_table_by_number.return_value = data
    mock_presenter.format_table_presenter.return_value = data
    
    response = client.get("/tables/1")

    assert response.status_code == 200
    assert response.json == {
            "id": 1,
            "table_number": 1,
            "table_status": "livre"
        }
    
    db_session.delete(table)
    db_session.commit()

def test_list_all_tables_controller(client, mocker, db_session):
    mock_list_table_composer = mocker.patch('src.composer.restaurant_table.list_all_table_composer')
    mock_service = mocker.Mock()
    mock_list_table_composer.return_value = mock_service
    
    mock_presenter_composer = mocker.patch('src.composer.restaurant_table_presenter_composer')
    mock_presenter = mocker.Mock()
    mock_presenter_composer.return_value = mock_presenter    

    table_one = RestaurantTable(table_number=1)
    db_session.add(table_one)
    db_session.commit()
    
    table_two = RestaurantTable(table_number=2)
    db_session.add(table_two)
    db_session.commit()

    data = [table_one, table_two]
    mock_service.list_all_table.return_value = data
    

    mock_presenter.format_all_table_presenter.return_value = [
        {"id": 1, "table_number": 1, "table_status": "livre"},
        {"id": 2, "table_number": 2, "table_status": "livre"},
    ]
    
    response = client.get("/tables/")

    assert response.status_code == 200
    assert response.json == [
        {"id": 1, "table_number": 1, "table_status": "livre"},
        {"id": 2, "table_number": 2, "table_status": "livre"},
    ]
    
    db_session.delete(table_one)
    db_session.delete(table_two)
    db_session.commit()