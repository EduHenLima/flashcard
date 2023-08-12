import json

from src.Model.Base.database import get_connection, get_session
from src.Model.categorias import Categorys


def delete(req, context):
    req = json.loads(req['body'])

    with get_session() as session:
        user = session.query(Categorys).filter(Categorys.id_categoria == req['pathParameters']['id_categoria']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['pathParameters']['id_categoria']),
    }

    return json.dumps({"statusCode": 200, "body": body})
