import json

from src.API.helpers.alchemyEncoder import AlchemyEncoder
from src.Model.Base.database import get_session
from src.Model.cards import Cards


def get_cards_by_topic(req, context):
    topics = get_session().query(Cards).filter(Cards.id_assunto == req['pathParameters']['id_topic'])
    result = topics.all()

    return json.dumps(result, cls=AlchemyEncoder)

