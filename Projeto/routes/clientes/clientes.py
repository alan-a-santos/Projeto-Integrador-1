from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/cadastro')
def cadastro():
    return render_template('clientes/clientes_cadastro.html')

@cliente_route.route('/consulta')
def consulta():
    return render_template('clientes/clientes_consulta.html')

@cliente_route.route('/atualiza')
def atualiza():
    return render_template('clientes/clientes_atualiza.html')

@cliente_route.route('/exclui')
def exclui():
    return render_template('clientes/clientes_exclui.html')

@cliente_route.route('/home')
def home1():
    return render_template('home.html')






