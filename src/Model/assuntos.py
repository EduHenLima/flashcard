from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Topics(Base):
    __tablename__ = 'assuntos'

    id_assunto = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, nullable=True)
    nome_assunto = Column(Integer, nullable=False)
    descricao = Column(Integer, nullable=True)
    ativo = Column(Integer, nullable=True)
    data_criacao = Column(Integer, nullable=True)
    data_atualizacao = Column(Integer, nullable=True)

