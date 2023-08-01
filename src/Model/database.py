import os

import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host=os.environ['host'],
        user=os.environ['user'],
        password=os.environ['password'],
        database=os.environ['database']
    )

