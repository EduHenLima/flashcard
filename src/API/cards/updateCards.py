import json

from src.Model.Base.database import get_connection, get_session
from src.Model.cards import Cards


def update(req, context):
    id_card = req['pathParameters']['id_card']
    body = json.loads(req['body'])

    with get_session() as session:
        session.query(Cards).filter(Cards.id_card == id_card).update({
            Cards.id_assunto: body['id_assunto'],
            Cards.pergunta: body['pergunta'],
            Cards.resposta: body['resposta'],
            Cards.ativo: body['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_card': id_card,
            'id_assunto': body['id_assunto'],
            'pergunta': body['pergunta'],
            'resposta': body['resposta'],
            'ativo': body['ativo']
        }
    }

    return json.dumps(body)
