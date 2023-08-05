from src.Model.database import get_connection


def update(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "UPDATE pergunta SET pergunta = %s WHERE id_pergunta = %s"
    val = (req['pergunta'], req['id_pergunta'])

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Update!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
