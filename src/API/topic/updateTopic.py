import json

from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def update(req, context):
    req = json.loads(req['body'])

    with get_session() as session:
        session.query(Topics).filter(Topics.id_assunto == req['id_assunto']).update({
            Topics.nome_assunto: req['nome_assunto'],
            Topics.descricao: req['descricao'],
            Topics.ativo: req['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'nome_assunto': req['nome_assunto'],
            'descricao': req['descricao'],
            'ativo': req['ativo']
        }
    }

    return {"statusCode": 200, "body": json.dumps(body)}
