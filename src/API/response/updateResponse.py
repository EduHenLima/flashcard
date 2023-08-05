from src.Model.database import get_connection


def update(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "UPDATE resposta SET resposta = %s WHERE id_resposta = %s"
    val = (req['resposta'],req['id_resposta'])

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
