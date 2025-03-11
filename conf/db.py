from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Отримуємо значення DATABASE_URL з .env файлу
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@postgres:5432/hw02"

# Створення двигуна для підключення до бази даних
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, max_overflow=5)

# Створення сесії для роботи з БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Основний клас для ORM
class Base(DeclarativeBase):
    pass

# Dependency для отримання сесії
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()