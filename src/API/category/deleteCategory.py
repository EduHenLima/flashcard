from src.Model.Base.database import get_connection, get_session
from src.Model.categorias import Categorys


def delete(req, context):
    with get_session() as session:
        user = session.query(Categorys).filter(Categorys.id_categoria == req['id_categoria']).one()
        session.delete(user)
        session.commit()

    body = {
        "message": "Success!",
        'Deleted': 'ID: ' + str(req['id_categoria']),
    }

    return {"statusCode": 200, "body": body}
