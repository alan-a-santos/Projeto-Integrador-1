from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/clientes')
def clientes():
    return render_template('/clientes/clientes.html')

@home_route.route('/pedidos')
def pedidos():
    return render_template('pedidos/pedidos.html')

@home_route.route('/logout')
def logout():
    return render_template('index.html')