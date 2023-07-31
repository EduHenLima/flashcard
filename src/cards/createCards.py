import json
import os


def create(event, context):
    abc = (os.environ['FOO']);
    body = {
        "message":  abc,
        "input": 'event',
    }

    return {"statusCode": 200, "body": json.dumps(body)}