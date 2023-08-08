from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Cards(Base):
    __tablename__ = 'cards'

    id_cards = Column(Integer, primary_key=True)
    pergunta = Column(String(255), nullable=False)
    resposta = Column(String(255), nullable=False)
    ativo = Column(Integer, primary_key=False)
    data_criacao = Column(Integer, primary_key=False)
    data_atualizacao = Column(Integer, primary_key=False)

