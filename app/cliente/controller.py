from app.cliente.models import Cliente
from flask.views import MethodView
from flask import request, jsonify, render_template
from flask_mail import Message
from app.extensions import mail

class ClienteG(MethodView):

    def post(self):
        body = request.json

        cpf = body.get('cpf')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        telefone = body.get('telefone')
        endereco = body.get('endereco')

        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(email, str):
            if isinstance(telefone, str) and isinstance(endereco, str):
                cliente = Cliente.query.filter_by(email=email).first()
                if cliente:
                    return {"code_status":"cliente already exists"}, 400
                cliente = Cliente(nome=nome, email=email, cpf=cpf, senha=senha, telefone=telefone, endereco=endereco)
                cliente.save()

                msg = Message(
                sender = 'ribeiro@poli.ufrj.br',
                recipients=[email],
                subject='Bem-vindo(a) ao Minerva Burguer!',
                html=render_template('email_cliente.html', nome=nome)
                )

                mail.send(msg)
                
                return cliente.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def get(self):
        clientes = Cliente.query.all()
        return jsonify([cliente.json() for cliente in clientes]), 200
    
class ClienteId(MethodView):

    def get(self, id):
        cliente = Cliente.query.get_or_404(id)
        return cliente.json()

    def put(self, id):
        body = request.json

        cpf = body.get('cpf')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        telefone = body.get('telefone')
        endereco = body.get('endereco')
        
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(email, str):
            if isinstance(telefone, str) and isinstance(endereco, str):
                cliente = Cliente.query.get_or_404(id)
                cliente.cpf = cpf
                cliente.nome = nome
                cliente.email = email
                cliente.senha = senha
                cliente.telefone = telefone
                cliente.endereco = endereco
                cliente.update()
                return cliente.json(), 200
        return {"code_status":"invalid data in request"}, 400

    def patch(self, id):
        body = request.json
        cliente = Cliente.query.get_or_404(id)

        cpf = body.get('cpf', cliente.cpf)
        nome = body.get('nome', cliente.nome)
        email = body.get('email', cliente.email)
        senha = body.get('senha', cliente.senha)
        telefone = body.get('telefone', cliente.telefone)
        endereco = body.get('endereco', cliente.endereco)
        
        if isinstance(cpf, str) and isinstance(nome, str) and isinstance(email, str):
            if isinstance(telefone, str) and isinstance(endereco, str):
                cliente.cpf = cpf
                cliente.nome = nome
                cliente.email = email
                cliente.senha = senha
                cliente.telefone = telefone
                cliente.endereco = endereco
                cliente.update()
                return cliente.json(), 200
        return {"code_status":"invalid data in request"}, 400
    
    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)
        return cliente.json()