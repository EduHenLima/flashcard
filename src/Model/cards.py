from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Cards(Base):
    __tablename__ = 'cards'

    id_card = Column(Integer, primary_key=True)
    id_assunto = Column(Integer, primary_key=True)
    pergunta = Column(String(255), nullable=True)
    resposta = Column(String(255), nullable=True)
    ativo = Column(Integer, nullable=True)
    data_criacao = Column(Integer, primary_key=True)
    data_atualizacao = Column(Integer, primary_key=True)

