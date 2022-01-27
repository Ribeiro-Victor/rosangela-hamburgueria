from app.funcionario.models import Funcionario
from flask.views import MethodView
from flask import request, jsonify, render_template
from flask_mail import Message
from app.extensions import mail

class FuncionarioG(MethodView):
    
    def post(self):
        body = request.json

        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')

        if isinstance(nome, str) and isinstance(email, str):
            funcionario = Funcionario.query.filter_by(email=email).first()
            if funcionario:
                return {"code_status":"funcionario already exists"}, 400
            funcionario = Funcionario(nome=nome, email=email, senha=senha)
            funcionario.save()

            msg = Message(
                sender = 'ribeiro@poli.ufrj.br',
                recipients=[email],
                subject='Bem-vindo a Minerva Burguer!',
                html=render_template('email.html', nome=nome)
            )

            mail.send(msg)

            return funcionario.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def get(self):
        funcionarios = Funcionario.query.all()
        return jsonify([funcionario.json() for funcionario in funcionarios]), 200

class FuncionarioId(MethodView):

    def get(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        return funcionario.json()

    def put(self, id):
        body = request.json

        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        
        if isinstance(nome, str) and isinstance(email, str):
            funcionario = Funcionario.query.get_or_404(id)
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha
            funcionario.update()
            return funcionario.json(), 200
        return {"code_status":"invalid data in request"}, 400

    def patch(self, id):
        body = request.json
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome', funcionario.nome)
        email = body.get('email', funcionario.email)
        senha = body.get('senha', funcionario.senha)
        
        if isinstance(nome, str) and isinstance(email, str):
            funcionario.nome = nome
            funcionario.email = email
            funcionario.senha = senha
            funcionario.update()
            return funcionario.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)
        return funcionario.json()