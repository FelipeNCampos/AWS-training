from abc import ABC, abstractmethod


@abstractmethod
class PasswordHasherInterface(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        """Gera um hash seguro para a senha fornecida."""

    @abstractmethod
    def verify(self, plain_password: str, hashed_password: str) -> bool:
        """Verifica se a senha fornecida corresponde ao hash armazenado."""