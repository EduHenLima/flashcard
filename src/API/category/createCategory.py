import json

from sqlalchemy import insert

from src.Model.Base.database import commit_insert
from src.Model.categorias import Categorys


def create(req, context):
    req = json.loads(req['body'])
    commit_insert(insert(Categorys).values(id_usuario=req['id_usuario'], nome_categoria=req['nome_categoria'], descricao=req['descricao'], ativo=req['ativo']))

    body = {
        "id_usuario": req['id_usuario'],
        "nome_categoria": req['nome_categoria'],
        "descricao": req['descricao'],
        "ativo":  req['ativo']
    }

    return json.dumps({"statusCode": 200, "body": body})
