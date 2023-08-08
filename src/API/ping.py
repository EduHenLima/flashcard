from sqlalchemy.exc import OperationalError
from src.Model.Base.database import get_connection


def pingDatabase(event, context):
    engine = get_connection()

    try:
        engine.connect()

        return print("Conexão bem-sucedida! O banco de dados está acessível.")
    except OperationalError as e:
        return print(f"Erro na conexão: {e}")
