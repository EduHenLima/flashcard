import json

from src.Model.Base.database import get_session
from src.Model.cards import Cards


def get_cards_by_topic(req, context):
    req = json.loads(req['body'])

    topics = get_session().query(Cards).filter(Cards.id_assunto == req['id_assunto'])
    for topic in topics:
        print(vars(topic))

    body = {
        "message": "Success!",
        "input": topics,
    }

    return json.dumps({"statusCode": 200, "body": body})
