from src.Model.database import get_connection


def update(req, context):
    connection = get_connection()
    mycursor = connection.cursor()
    sql = "UPDATE assuntos SET id_categoria = %s, tipo = %s, nome_assunto = %s, descricao = %s, ativo = %s WHERE id_assunto = %s"
    val = (req['id_categoria'], req['tipo'], req['nome_assunto'],req['descricao'], req['ativo'], req['id_assunto'])

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
