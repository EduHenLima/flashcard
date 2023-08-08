from src.Model.Base.database import get_session
from src.Model.categorias import Categorys


def update(req, context):
    with get_session() as session:
        session.query(Categorys).filter(Categorys.id_categoria == req['id_categoria']).update({
            Categorys.id_usuario: req['id_usuario'],
            Categorys.nome_categoria: req['nome_categoria'],
            Categorys.descricao: req['descricao'],
            Categorys.ativo: req['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_usuario': req['id_usuario'],
            'nome_categoria': req['nome_categoria'],
            'descricao': req['descricao'],
            'ativo': req['ativo']
        }
    }

    return {"statusCode": 200, "body": body}
