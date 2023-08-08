from src.Model.Base.database import get_connection


def create(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "INSERT INTO categorias (id_usuario,nome_categoria,descricao,ativo) VALUES (%s,%s,%s,%s)"
    val = (req['id_usuario'], req['nome_categoria'], req['descricao'], req['ativo'])
    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
