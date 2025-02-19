from src.models.users import Users
from src.models.base import db

class UsersRepository:
    def __init__(self):
        self.__session = db.session
    
    def create_user(self, data):
        new_user = Users(username = data['username'], password=data['password'])
        self.__session.add(new_user)
        self.__session.commit()
    