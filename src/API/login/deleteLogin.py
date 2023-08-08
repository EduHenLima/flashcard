import json

from src.Model.Base.database import get_session
from src.Model.login import Login


def delete(req, context):
    with get_session() as session:
        user = session.query(Login).filter(Login.id_usuario == req['id_usuario']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['id_usuario']),
    }

    return {"statusCode": 200, "body": body}

