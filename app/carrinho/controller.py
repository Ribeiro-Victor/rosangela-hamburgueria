from app.carrinho.models import Carrinho
from flask.views import MethodView
from flask import request, jsonify

class CarrinhoG(MethodView):
    
    def post(self):
        body = request.json

        precoTotal = body.get('precoTotal')
        id_cliente = body.get('id_cliente')

        if isinstance(precoTotal, float) and isinstance(id_cliente, int):
            carrinho = Carrinho(precoTotal=precoTotal, id_cliente=id_cliente)
            carrinho.save()
            return carrinho.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def get(self):
        carrinhos = Carrinho.query.all()
        return jsonify([carrinho.json() for carrinho in carrinhos]), 200

class CarrinhoId(MethodView):

    def get(self, id):
        carrinho = Carrinho.query.get_or_404(id)
        return carrinho.json()

    def put(self, id):
        body = request.json

        precoTotal = body.get('precoTotal')
        id_cliente = body.get('id_cliente')
        
        if isinstance(precoTotal, float) and isinstance(id_cliente, int):
            carrinho = Carrinho.query.get_or_404(id)
            carrinho.precoTotal = precoTotal
            carrinho.id_cliente = id_cliente
            carrinho.update()
            return carrinho.json(), 200
        return {"code_status":"invalid data in request"}, 400

    def patch(self, id):
        body = request.json
        carrinho = Carrinho.query.get_or_404(id)

        precoTotal = body.get('precoTotal', carrinho.precoTotal)
        id_cliente = body.get('id_cliente', carrinho.id_cliente)
        
        if isinstance(precoTotal, float) and isinstance(id_cliente, int):
            carrinho.precoTotal = precoTotal
            carrinho.id_cliente = id_cliente
            carrinho.update()
            return carrinho.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def delete(self, id):
        carrinho = Carrinho.query.get_or_404(id)
        carrinho.delete(carrinho)
        return carrinho.json()