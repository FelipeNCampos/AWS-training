from src.modules.auth.application.dtos import RegisterUserInputDTO, UserOutputDTO
from src.modules.auth.application.ports import PasswordHasherInterface
from src.modules.auth.domain.entities import User
from src.modules.auth.domain.interfaces import UserRepositoryInterface


class RegisterUserUseCase:
    def __init__(
            self,
            user_repository: UserRepositoryInterface, 
            password_hasher: PasswordHasherInterface
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, input_dto: RegisterUserInputDTO) -> UserOutputDTO:
        existing_user = self.user_repository.find_by_email(input_dto.email)
        if existing_user:
            raise ValueError("Usuário com este e-mail já existe.")

        hashed_password = self.password_hasher.hash(input_dto.password)

        new_user = User(email=input_dto.email, hashed_password=hashed_password)

        saved_user = self.user_repository.save(new_user)

        return UserOutputDTO(id=saved_user.id, email=saved_user.email, is_active=saved_user.is_active)


class LoginUserUseCase:
    def __init__(
            self,
            user_repository: UserRepositoryInterface, 
            password_hasher: PasswordHasherInterface
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher

    def execute(self, email: str, password: str) -> UserOutputDTO:
        user = self.user_repository.find_by_email(email)
        if not user:
            self.password_hasher.hash(password)  # Hashing the password to mitigate timing attacks
            raise ValueError("Usuário não encontrado.")


        if not self.password_hasher.verify(password, user.hashed_password):
            raise ValueError("Senha incorreta.")

        return UserOutputDTO(id=user.id, email=user.email, is_active=user.is_active)