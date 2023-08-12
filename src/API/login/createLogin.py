import json

from sqlalchemy import insert
from src.Model.Base.database import commit_insert
from src.Model.login import Login


def create(req, context):
    req = json.loads(req['body'])
    commit_insert(insert(Login).values(email=req['email'], uui=req['uui']))

    body = {
        "email": req['email'],
        "uui": req['uui'],
    }

    return json.dumps(body)
