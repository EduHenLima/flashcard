from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Topics(Base):
    __tablename__ = 'assuntos'

    id_assunto = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, primary_key=False)
    nome_assunto = Column(Integer, primary_key=False)
    descricao = Column(Integer, primary_key=False)
    ativo = Column(Integer, primary_key=False)
    data_criacao = Column(Integer, primary_key=False)
    data_atualizacao = Column(Integer, primary_key=False)

