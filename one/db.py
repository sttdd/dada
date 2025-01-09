from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base() # Создаем базовый класс для моделей

# Класс Connect для работы с базой данных
class Connect:
    @staticmethod #создание статич метода внутри класса
    def create_connection():
        engine = create_engine("postgresql://postgres:1234@localhost:5432/bez")#подключение к базе данных (убрать пароль)
        Base.metadata.create_all(engine)# Создание таблиц в базе данных, если они еще не существуют
        Session = sessionmaker(bind=engine)
        session = Session() #объект сессии для выполнения запросов 
        return session

# Определение модели Dolzn
class Dolzn(Base):
    __tablename__ = 'dolzn'  # название таблицы как в бд
    
    id = Column(Integer, primary_key=True) #название как в бд
    name = Column(String(255), nullable=False) #название как в бд

# Определение модели User
class User(Base):
    __tablename__ = 'users'  # название таблицы как в бд

    id = Column(Integer, primary_key=True) #опред название как в бд
    full_name = Column(String(100), nullable=False) #опред название как в бд
    email = Column(String(100), unique=True, nullable=False) #опред название как в бд
    phone_number = Column(String(15), nullable=False) #опред название как в бд
    dol_id = Column(Integer, ForeignKey('dolzn.id'))  # связь с таблицей dolzn
    created_at = Column(TIMESTAMP, default="CURRENT_TIMESTAMP") #опред название как в бд

    # Связь с таблицей Dolzn
    dolzn = relationship("Dolzn", back_populates="users")

Dolzn.users = relationship("User", order_by=User.id, back_populates="dolzn")
