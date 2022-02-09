from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# SQLALCHEMY_DATABASE_URL = "fastapi_1:///./test.db"
# SQLALCHEMY_DATABASE_URL = "sqlite://"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )


# engine = create_engine('sqlite:///:memory:?cache=shared&check_same_thread=False',
engine = create_engine('sqlite:///file:memDB1?cache=shared',
                       echo_pool=True, echo=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

# session_factory = sessionmaker(bind=engine)
# SessionLocal = scoped_session(session_factory)
