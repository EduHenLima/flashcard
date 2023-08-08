from sqlalchemy import delete, text

from src.Model.Base.database import get_connection, get_session
from src.Model.assuntos import Topics


def delete(req, context):
    with get_session() as session:
        user = session.query(Topics).filter(Topics.id_assunto == req['id_assunto']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['id_assunto']),
    }

    return {"statusCode": 200, "body": body}
