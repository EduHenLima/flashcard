import json

from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def get_topic_by_category(req, context):
    req = json.loads(req['body'])

    topics = get_session().query(Topics).filter(Topics.id_categoria == req['id_categoria'])
    for topic in topics:
        print(vars(topic))

    body = {
        "message": "Success!",
        "input": topics,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
