from src.repositories.users.users_repository import UsersRepository
from src.utils import bcrypt

class CreateUserService:
    def __init__(self, users_repository: UsersRepository):
        self.__users_repository = users_repository
    
    def create_user(self, data):
        if 'password' in data:
            data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        return self.__users_repository.create_user(data)