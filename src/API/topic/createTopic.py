from sqlalchemy import insert
from src.Model.Base.database import commit_insert
from src.Model.assuntos import Topics


def create(req, context):
    createTopic = insert(Topics).values(id_categoria=req['id_categoria'], nome_assunto=req['nome_assunto'], descricao=req['descricao'],ativo=req['ativo'])

    body = {
        "message": "Success!",
        'Quantity': commit_insert(createTopic),
    }

    return {"statusCode": 200, "body": body}
