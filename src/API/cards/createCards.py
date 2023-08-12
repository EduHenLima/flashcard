import json

from sqlalchemy import insert

from src.Model.Base.database import commit_insert
from src.Model.cards import Cards


def create(req, context):
    req = json.loads(req['body'])

    commit_insert(insert(Cards).values(pergunta=req['pergunta'], resposta=req['resposta'], id_assunto=req['id_assunto'], ativo=req['ativo']))

    body = {
        "message": "Success!",
        "Created": {
            "pergunta": req['pergunta'],
            "resposta": req['resposta'],
            "id_assunto": req['id_assunto'],
            "ativo":  req['ativo']
        },
    }

    return {"statusCode": 200, "body": json.dumps(body)}
