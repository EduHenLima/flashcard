from src.Model.Base.database import get_connection


def update(req, context):
    connection = get_connection()
    mycursor = connection.cursor()

    sql = "UPDATE categorias SET id_usuario = %s, nome_categoria = %s, descricao = %s, ativo = %s WHERE id_categoria = %s"
    val = (req['id_usuario'], req['nome_categoria'], req['descricao'], req['ativo'], req['id_categoria'])

    mycursor.execute(sql, val)
    connection.commit()

    body = {
        "message": "Success!",
        'Quantity': mycursor.rowcount,
    }

    return {"statusCode": 200, "body": body}
