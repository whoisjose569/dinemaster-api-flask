from src.repositories.users.users_repository import UsersRepository
from src.domain.users_use_cases.create_user import CreateUserService

def create_user_composer():
    repo = UsersRepository()
    service = CreateUserService(repo)
    return service