from src.Model.database import get_connection


def create(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "INSERT INTO pergunta (pergunta) VALUES (%s)"
    val = (req['pergunta'],)
    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Create!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
