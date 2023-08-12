import json

from src.Model.Base.database import get_session
from src.Model.assuntos import Topics


def delete(req, context):
    req = json.loads(req['body'])

    with get_session() as session:
        user = session.query(Topics).filter(Topics.id_assunto == req['id_assunto']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['id_assunto']),
    }

    return json.dumps({"statusCode": 200, "body": body})
