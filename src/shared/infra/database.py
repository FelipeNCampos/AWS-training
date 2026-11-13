from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Em um projeto real, essa URL vem do arquivo .env (usando os.getenv ou pydantic-settings)
SQLALCHEMY_DATABASE_URL = "sqlite:///./banco_de_dados.db" 
# Exemplo Postgres: "postgresql://usuario:senha@localhost:5432/meubanco"

# Cria o motor de conexão com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Fabrica as sessões (o "Session" que injetamos no repositório vem daqui)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# O molde oficial que todas as tabelas do sistema inteiro vão usar
Base = declarative_base()