import json

from src.Model.Base.database import get_session
from src.Model.login import Login


def update(req, context):
    req = json.loads(req['body'])

    with get_session() as session:
        session.query(Login).filter(Login.id_usuario == req['id_usuario']).update({
            Login.email: req['email'],
            Login.uui: req['uui'],
        })
        session.commit()

    body = {
        "message": "Success!",
        'Params Updated': {
            'id_usuario': req['id_usuario'],
            'email': req['email'],
            'uui': req['uui'],
        }
    }

    return json.dumps({"statusCode": 200, "body": body})
