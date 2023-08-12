import json

from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def read(event, context):
    topics = get_session().query(Topics)
    for topic in topics:
        print(vars(topic))

    body = {
        "message": "Success!",
        "input": topics,
    }

    return json.dumps({"statusCode": 200, "body": body})
