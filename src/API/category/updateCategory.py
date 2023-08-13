import json
from sqlalchemy import update

from src.Model.Base.database import get_session
from src.Model.categorias import Categorys


def updated(req, context):
    id_categoria = req['pathParameters']['id_category']
    body = json.loads(req['body'])

    with get_session() as session:
        session.query(Categorys).filter(Categorys.id_categoria == id_categoria).update({
            Categorys.id_usuario: body['id_usuario'],
            Categorys.nome_categoria: body['nome_categoria'],
            Categorys.descricao: body['descricao'],
            Categorys.ativo: body['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_categoria': id_categoria,
            'id_usuario': body['id_usuario'],
            'nome_categoria': body['nome_categoria'],
            'descricao': body['descricao'],
            'ativo': body['ativo']
        }
    }

    return json.dumps(body)
