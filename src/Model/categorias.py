from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Categorys(Base):
    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=True)
    nome_categoria = Column(String(45), nullable=False)
    descricao = Column(String(255), nullable=False)
    ativo = Column(Integer, nullable=False)
    data_criacao = Column(Integer, nullable=True)
    data_atualizacao = Column(Integer, nullable=True)

