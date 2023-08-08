from sqlalchemy import insert

from src.Model.Base.database import commit_insert
from src.Model.categorias import Categorys


def create(req, context):

    commit_insert(insert(Categorys).values(id_usuario=req['id_usuario'], nome_categoria=req['nome_categoria'], descricao=req['descricao'], ativo=req['ativo']))

    body = {
        "message": "Success!",
        "Created": {
            "id_usuario": req['id_usuario'],
            "nome_categoria": req['nome_categoria'],
            "descricao": req['descricao'],
            "ativo":  req['ativo']
        },
    }

    return {"statusCode": 200, "body": body}
