import os
from ..Model.database import get_connection


def pingDatabase(event, context):

    ping = (get_connection().ping(reconnect=False, attempts=1, delay=0))

    if ping is None:
        return "Connection with Success"
    else:
        return "The connection is refused"
