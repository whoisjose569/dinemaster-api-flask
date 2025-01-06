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

    print(response.json)
    
    assert response.status_code == HTTPStatus.CREATED
    
    assert response.json == {
            "id": 1,
            "msg": 'RestaurantTable created!.',
            "table_number": 1,
            "table_status": "livre"
        }

    table_in_db = db_session.query(RestaurantTable).filter_by(table_number=1).first()
    db_session.delete(table_in_db)
    db_session.commit()
    

    
    
    