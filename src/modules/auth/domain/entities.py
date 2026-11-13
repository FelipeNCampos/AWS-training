import uuid
from dataclasses import dataclass, field


@dataclass
class User:
    email: str
    hashed_password: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    is_active: bool = True

    def __post_init__(self):
        if "@" not in self.email:
            raise ValueError("O formato do e-mail é inválido nas regras de negócio.")