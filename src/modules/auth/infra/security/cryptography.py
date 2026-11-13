from passlib.context import CryptContext

from src.modules.auth.application.ports import PasswordHasherInterface

# Configuração do Passlib para usar Bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class BcryptPasswordHasher(PasswordHasherInterface):
    def hash(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)