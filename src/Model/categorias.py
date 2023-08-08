from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Categorys(Base):
    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True, nullable=False)
    id_usuario = Column(Integer, nullable=True)
    nome_categoria = Column(Integer, nullable=False)
    descricao = Column(Integer, Nullable=True)
    ativo = Column(Integer, Nullable=False)
    data_criacao = Column(Integer, Nullable=False)
    data_atualizacao = Column(Integer, Nullable=False)

