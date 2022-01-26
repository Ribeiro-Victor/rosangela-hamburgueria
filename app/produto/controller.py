from math import prod
from app.produto.models import Produto
from flask.views import MethodView
from flask import request, jsonify

class ProdutoG(MethodView):
    
    def post(self):
        body = request.json

        nome = body.get('nome')
        descricao = body.get('descricao')
        preco = body.get('preco')

        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(preco, float):
            produto = Produto(nome=nome, descricao=descricao, preco=preco)
            produto.save()
            return produto.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def get(self):
        produtos = Produto.query.all()
        return jsonify([produto.json() for produto in produtos]), 200

class ProdutoId(MethodView):

    def get(self, id):
        produto = Produto.query.get_or_404(id)
        return produto.json()

    def put(self, id):
        body = request.json

        nome = body.get('nome')
        descricao = body.get('descricao')
        preco = body.get('preco')
        
        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(preco, float):
            produto = Produto.query.get_or_404(id)
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            produto.update()
            return produto.json(), 200
        return {"code_status":"invalid data in request"}, 400

    def patch(self, id):
        body = request.json
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome', produto.nome)
        descricao = body.get('descricao', produto.descricao)
        preco = body.get('preco', produto.preco)
        
        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(preco, float):
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            produto.update()
            return produto.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)
        return produto.json()