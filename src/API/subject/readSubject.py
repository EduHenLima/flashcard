from src.Model.database import get_connection


def read(event, context):
    connection = get_connection()
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM assuntos")
    myresult = mycursor.fetchall()

    body = {
        "message": "Success!",
        "input": myresult,
    }

    return {"statusCode": 200, "body": body}
