from flask import Blueprint, render_template,request
import mysql.connector

consulta_route = Blueprint('consulta', __name__)

@consulta_route.route('/consulta')
def dados():
    cliente = request.form['nome']
    print(cliente)
    
# @consulta_route.route('/home1')
# def home1():
#     return render_template('home.html')

# @consulta_route.route('/home1')
# def home():
#     return render_template('home.html')

# @consulta_route.route('/atualiza')
# def atualizar():
#     return render_template('clientes/clientes_atualiza.html')

# @consulta_route.route('/consulta')
# def consultar():
#     return render_template('clientes/clientes_consulta.html')

# @consulta_route.route('/exclui')
# def excluir():
#     return render_template('clientes/clientes_exclui.html')
