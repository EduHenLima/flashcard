import json

from src.API.helpers.alchemyEncoder import AlchemyEncoder
from src.Model.Base.database import get_session
from src.Model.categorias import Categorys


def get_category_by_user(req, context):
    categorys = get_session().query(Categorys).filter(Categorys.id_usuario == req['pathParameters']['id_usuario'])
    result = categorys.all()

    return json.dumps(result, cls=AlchemyEncoder)
