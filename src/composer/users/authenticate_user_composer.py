from src.repositories.users.users_repository import UsersRepository
from src.domain.users_use_cases.authenticate_user import AuthenticateUserService

def authenticate_user_composer():
    repo = UsersRepository()
    service = AuthenticateUserService(repo)
    return service