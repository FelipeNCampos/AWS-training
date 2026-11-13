from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.shared.infra.database import Base


class UserModel(Base):
    __tablename__ = "users"

    # Usando Mapped[tipo] o VS Code entende perfeitamente que isso vai virar uma string ou bool
    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(default=True)