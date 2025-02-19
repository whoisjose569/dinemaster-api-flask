from src.repositories.users.users_repository import UsersRepository
from src.utils import bcrypt
from flask_jwt_extended import create_access_token
from src.errors.custom_errors import UserNotFound, UserWrongPassword

class AuthenticateUserService:
    def __init__(self, users_repository: UsersRepository):
        self.__users_repository = users_repository
    
    def authenticate_user(self, data):
        user_on_db = self.__users_repository.get_by_username(data['username'])
        if not user_on_db:
            raise UserNotFound()
        
        if not bcrypt.check_password_hash(user_on_db.password, data['password']):
            raise UserWrongPassword()
        
        access_token = create_access_token(identity=data['username'])
        
        return {"access_token": access_token, "user_id": user_on_db.id}