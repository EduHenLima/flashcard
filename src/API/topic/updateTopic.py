import json

from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def update(req, context):
    id_topic = req['pathParameters']['id_topic']
    body = json.loads(req['body'])

    with get_session() as session:
        session.query(Topics).filter(Topics.id_assunto == id_topic).update({
            Topics.nome_assunto: body['nome_assunto'],
            Topics.descricao: body['descricao'],
            Topics.ativo: body['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_assunto': id_topic,
            'nome_assunto': body['nome_assunto'],
            'descricao': body['descricao'],
            'ativo': body['ativo']
        }
    }

    return json.dumps(body)
