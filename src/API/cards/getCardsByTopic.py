from src.Model.Base.database import get_session
from src.Model.cards import Cards
from src.Model.categorias import Categorys


def get_cards_by_topic(req, context):
    topics = get_session().query(Cards).filter(Cards.id_assunto == req['id_assunto'])
    for topic in topics:
        print(vars(topic))

    body = {
        "message": "Success!",
        "input": topics,
    }

    return {"statusCode": 200, "body": body}
