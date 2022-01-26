from flask import Blueprint
from app.alimento.controller import AlimentoG, AlimentoId

alimento_api = Blueprint('alimento_api', __name__)

alimento_api.add_url_rule('/alimento', view_func = AlimentoG.as_view('alimento_geral'), methods = ['POST', 'GET'])

alimento_api.add_url_rule('/alimento/<int:id>', view_func = AlimentoId.as_view('alimento_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
