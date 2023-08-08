from src.Model.Base.database import get_session
from src.Model.categorias import Categorys


def get_category_by_user(req, context):
    categorys = get_session().query(Categorys).filter(Categorys.id_usuario == req['id_usuario'])
    for category in categorys:
        print(vars(category))

    body = {
        "message": "Success!",
        "input": categorys,
    }

    return {"statusCode": 200, "body": body}
