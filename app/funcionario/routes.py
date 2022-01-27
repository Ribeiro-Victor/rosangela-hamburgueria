from flask import Blueprint
from app.funcionario.controller import FuncionarioG, FuncionarioId, FuncionarioLogin

funcionario_api = Blueprint('funcionario_api', __name__)

funcionario_api.add_url_rule('/funcionario', view_func = FuncionarioG.as_view('funcionario_geral'), methods = ['POST', 'GET'])

funcionario_api.add_url_rule('/funcionario/<int:id>', view_func = FuncionarioId.as_view('funcionario_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

funcionario_api.add_url_rule('/login', view_func = FuncionarioLogin.as_view('funcionario_login'), methods = ['POST'])
