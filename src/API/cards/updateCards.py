from src.Model.database import get_connection


def update(req, context):
    connection = get_connection()
    mycursor = connection.cursor()
    sql = "UPDATE cards SET id_pergunta = %s, id_resposta = %s, id_assunto = %s, ativo = %s WHERE id_cards = %s"
    val = (req['id_pergunta'], req['id_resposta'], req['id_assunto'], req['ativo'], req['id_cards'])

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Updated!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
