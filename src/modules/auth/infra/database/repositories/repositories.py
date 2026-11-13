from sqlalchemy.orm import Session

from modules.auth.infra.database.models import UserModel
from src.modules.auth.domain.entities import User
from src.modules.auth.domain.interfaces import UserRepositoryInterface


class SQLAlchemyUserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        # A sessão do banco é injetada aqui. O repositório não abre nem fecha a conexão, 
        # ele apenas a utiliza.
        self.session = session

    def save(self, user: User) -> User:
        """
        Pega a Entidade do domínio, traduz para o Modelo do banco e salva.
        """
        user_model = UserModel(
            id=user.id,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=user.is_active
        )
        
        # session.merge() é excelente: se o ID não existir no banco, ele faz INSERT.
        # Se o ID já existir, ele atualiza as colunas necessárias (UPDATE).
        self.session.merge(user_model)
        self.session.commit()
        
        return user

    def get_by_email(self, email: str) -> User | None:
        """
        Busca o usuário no banco pelo e-mail e devolve como Entidade de Domínio.
        """
        model = self.session.query(UserModel).filter(UserModel.email == email).first()
        
        if not model:
            return None
            
        return self._to_domain(model)

    def get_by_id(self, user_id: str) -> User | None:
        """
        Busca o usuário no banco pelo ID e devolve como Entidade de Domínio.
        """
        model = self.session.query(UserModel).filter(UserModel.id == user_id).first()
        
        if not model:
            return None
            
        return self._to_domain(model)

    # -------------------------------------------------------------------------
    # Método Auxiliar Privado
    # -------------------------------------------------------------------------
    def _to_domain(self, model: UserModel) -> User:
        """
        Reconstrói a classe pura do Python (dataclass) a partir do registro do banco.
        Assim, o Caso de Uso recebe exatamente a entidade que ele espera trabalhar.
        """
        return User(
            email=model.email,
            hashed_password=model.hashed_password,
            id=model.id,
            is_active=model.is_active
        )