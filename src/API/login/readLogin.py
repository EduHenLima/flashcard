from src.Model.Base.database import get_session
from src.Model.login import Login


def read(event, context):
    logins = get_session().query(Login)
    for login in logins:
        print(vars(login))

    body = {
        "message": "Success!",
        "input": logins,
    }

    return {"statusCode": 200, "body": body}
