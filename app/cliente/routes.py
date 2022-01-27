from flask import Blueprint
from app.cliente.controller import ClienteG, ClienteId, ClienteLogin

cliente_api = Blueprint('cliente_api', __name__)

cliente_api.add_url_rule('/cliente', view_func = ClienteG.as_view('cliente_geral'), methods = ['POST', 'GET'])

cliente_api.add_url_rule('/cliente/<int:id>', view_func = ClienteId.as_view('cliente_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])

cliente_api.add_url_rule('/login-cliente', view_func = ClienteLogin.as_view('cliente_login'), methods = ['POST'])