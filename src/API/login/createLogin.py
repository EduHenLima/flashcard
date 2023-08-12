import json

from sqlalchemy import insert
from src.Model.Base.database import commit_insert
from src.Model.login import Login


def create(req, context):
    req = json.loads(req['body'])
    commit_insert(insert(Login).values(email=req['email'], uui=req['uui']))

    body = {
        "message": "Success!",
        "Created": {
            "email": req['email'],
            "uui": req['uui'],
        },
    }

    return {"statusCode": 200, "body": json.dumps(body)}
