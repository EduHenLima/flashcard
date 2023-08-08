from src.Model.Base.database import get_connection, get_session
from src.Model.cards import Cards


def update(req, context):
    with get_session() as session:
        session.query(Cards).filter(Cards.id_card == req['id_card']).update({
            Cards.id_assunto: req['id_assunto'],
            Cards.pergunta: req['pergunta'],
            Cards.resposta: req['resposta'],
            Cards.ativo: req['ativo']
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_assunto': req['id_assunto'],
            'pergunta': req['pergunta'],
            'resposta': req['resposta'],
            'ativo': req['ativo']
        }
    }

    return {"statusCode": 200, "body": body}
