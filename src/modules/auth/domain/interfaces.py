from abc import ABC, abstractmethod

from src.modules.auth.domain.entities import User


class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def save(self, user: User) -> User:
        """Salva um novo usuário ou atualiza um existente."""

    @abstractmethod
    def delete(self, user_id: str) -> None:
        """Deleta um usuário pelo ID."""

    @abstractmethod
    def find_by_email(self, email: str) -> User | None:
        """Encontra um usuário pelo e-mail. Retorna None se não encontrar"""

    @abstractmethod
    def find_by_id(self, user_id: str) -> User | None:
        """Encontra um usuário pelo ID. Retorna None se não encontrar"""
