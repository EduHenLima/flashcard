from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Login(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(255), nullable=True)
    uui = Column(Integer, nullable=True)
