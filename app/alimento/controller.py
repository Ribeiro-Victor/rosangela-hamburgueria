from app.alimento.models import Alimento
from flask.views import MethodView
from flask import request, jsonify

class AlimentoG(MethodView):
    
    def post(self):
        body = request.json

        nome = body.get('nome')
        descricao = body.get('descricao')
        quantidade = body.get('quantidade')

        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(quantidade, int):
            alimento = Alimento(nome=nome, descricao=descricao, quantidade=quantidade)
            alimento.save()
            return alimento.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def get(self):
        alimentos = Alimento.query.all()
        return jsonify([alimento.json() for alimento in alimentos]), 200

class AlimentoId(MethodView):

    def get(self, id):
        alimento = Alimento.query.get_or_404(id)
        return alimento.json()

    def put(self, id):
        body = request.json

        nome = body.get('nome')
        descricao = body.get('descricao')
        quantidade = body.get('quantidade')
        
        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(quantidade, int):
            alimento = Alimento.query.get_or_404(id)
            alimento.nome = nome
            alimento.descricao = descricao
            alimento.quantidade = quantidade
            alimento.update()
            return alimento.json(), 200
        return {"code_status":"invalid data in request"}, 400

    def patch(self, id):
        body = request.json
        alimento = Alimento.query.get_or_404(id)

        nome = body.get('nome', alimento.nome)
        descricao = body.get('descricao', alimento.descricao)
        quantidade = body.get('quantidade', alimento.quantidade)
        
        if isinstance(nome, str) and isinstance(descricao, str) and isinstance(quantidade, int):
            alimento.nome = nome
            alimento.descricao = descricao
            alimento.quantidade = quantidade
            alimento.update()
            return alimento.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def delete(self, id):
        alimento = Alimento.query.get_or_404(id)
        alimento.delete(alimento)
        return alimento.json()