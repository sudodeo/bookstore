from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from ..config import settings

engine = create_engine(settings.POSTGRESQL_CONN_STRING)
test_engine = create_engine(settings.POSTGRESQL_TEST_CONN_STRING)
if settings.APP_ENV == "test":
    engine = test_engine
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    if settings.APP_ENV == "test":
        db = TestSessionLocal()
    else:
        db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_test_session():
    return TestSessionLocal()


def drop_test_database():
    Base.metadata.drop_all(bind=test_engine)
