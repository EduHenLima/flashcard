import json

from src.Model.Base.database import get_connection, get_session
from src.Model.cards import Cards


def delete(req, context):
    req = json.loads(req['body'])

    with get_session() as session:
        user = session.query(Cards).filter(Cards.id_cards == req['id_cards']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['id_cards']),
    }

    return json.dumps({"statusCode": 200, "body": body})
