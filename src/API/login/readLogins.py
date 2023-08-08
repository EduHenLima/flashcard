import json

from src.Model.Base.database import get_session
from src.Model.logins import Login


def read(event, context):
    categorys = get_session().query(Login)
    for category in categorys:
        print(vars(category))

    body = {
        "message": "Success!",
        "input": categorys,
    }

    return {"statusCode": 200, "body": body}

