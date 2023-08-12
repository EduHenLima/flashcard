import json

from src.Model.Base.database import get_session
from src.Model.cards import Cards


def read(event, context):
    cards = get_session().query(Cards)
    for card in cards:
        print(vars(card))

    body = {
        "message": "Success!",
        "input": cards,
    }

    return json.dumps({"statusCode": 200, "body": body})
