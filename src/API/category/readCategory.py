import json
from src.Model.Base.database import get_session
from src.Model.categorias import Categorys


def read(event, context):
    categorys = get_session().query(Categorys)
    for category in categorys:
        print(vars(category))

    body = {
        "message": "Success!",
        "input": categorys,
    }

    return json.dumps({"statusCode": 200, "body": body})
