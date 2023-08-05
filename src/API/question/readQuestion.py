from src.Model.database import get_connection


def read(event, context):
    connection = get_connection()
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM pergunta")
    myresult = mycursor.fetchone()

    body = {
        "message": "Visualized",
        "input": myresult,
    }

    return {"statusCode": 200, "body": body}
