from src.Model.database import get_connection


def delete(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "DELETE FROM cards WHERE id_cards = %s"
    val = (req['id_cards'],)

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
