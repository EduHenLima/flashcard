import json

from src.API.helpers.alchemyEncoder import AlchemyEncoder
from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def get_topic_by_category(req, context):
    topics = get_session().query(Topics).filter(Topics.id_categoria == req['pathParameters']['id_categoria'])
    result = topics.all()

    return json.dumps(result, cls=AlchemyEncoder)
