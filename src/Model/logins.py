from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Login(Base):
    __tablename__ = 'usuarios'

    id_usuário = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    uui = Column(Integer, primary_key=True)
