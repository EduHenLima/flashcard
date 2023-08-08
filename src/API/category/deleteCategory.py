from src.Model.Base.database import get_connection


def delete(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "DELETE FROM categorias WHERE id_categoria = %s"
    val = (req['id_categoria'],)

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
