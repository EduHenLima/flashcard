from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Categorys(Base):
    __tablename__ = 'categorias'

    id_categoria = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, primary_key=False)
    nome_categoria = Column(Integer, primary_key=False)
    descricao = Column(Integer, primary_key=False)
    ativo = Column(Integer, primary_key=False)
    data_criacao = Column(Integer, primary_key=False)
    data_atualizacao = Column(Integer, primary_key=False)

