from src.Model.database import get_connection


def create(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "INSERT INTO assuntos (id_categoria,tipo,nome_assunto,descricao,ativo) VALUES (%s,%s,%s,%s,%s)"
    val = (req['id_categoria'], req['tipo'], req['nome_assunto'], req['descricao'], req['ativo'])
    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Create!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
