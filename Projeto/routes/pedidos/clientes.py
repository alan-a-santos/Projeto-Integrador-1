from flask import Blueprint, render_template

pedido_route = Blueprint('pedido', __name__)

@pedido_route.route('/incluir')
def incluir():
    return render_template('pedidos/pedidos_cadastro.html')

@pedido_route.route('/consultap')
def consultar():
    return render_template('pedidos/pedidos_consulta.html')

@pedido_route.route('/atualizap')
def atualizar():
    return render_template('pedidos/pedidos_atualiza.html')

@pedido_route.route('/excluip')
def excluir():
    return render_template('pedidos/pedidos_exclui.html')

# @cliente_route.route('/home1')
# def home():
#     return render_template('home.html')




