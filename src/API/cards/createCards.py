from src.Model.database import get_connection


def create(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "INSERT INTO cards (id_pergunta,id_resposta,id_assunto,ativo) VALUES (%s,%s,%s,%s)"
    val = (req['id_pergunta'], req['id_resposta'], req['id_assunto'], req['ativo'])
    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
