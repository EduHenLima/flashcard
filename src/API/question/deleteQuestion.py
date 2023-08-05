from src.Model.database import get_connection


def delete(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "DELETE FROM pergunta WHERE id_pergunta = %s"
    val = (req['id_pergunta'],)

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
