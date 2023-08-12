import json

from sqlalchemy import insert

from src.Model.Base.database import commit_insert
from src.Model.assuntos import Topics


def create(req, context):
    req = json.loads(req['body'])

    commit_insert(insert(Topics).values(id_categoria=req['id_categoria'], nome_assunto=req['nome_assunto'], descricao=req['descricao'],ativo=req['ativo']))

    body = {
        "id_categoria": req['id_categoria'],
        "nome_assunto": req['nome_assunto'],
        "descricao": req['descricao'],
        "ativo":  req['ativo']
    }

    return json.dumps({"statusCode": 200, "body": body})
