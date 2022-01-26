from flask import Blueprint
from app.carrinho.controller import CarrinhoG, CarrinhoId

carrinho_api = Blueprint('carrinho_api', __name__)

carrinho_api.add_url_rule('/carrinho', view_func = CarrinhoG.as_view('carrinho_geral'), methods = ['POST', 'GET'])

carrinho_api.add_url_rule('/carrinho/<int:id>', view_func = CarrinhoId.as_view('carrinho_id'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
