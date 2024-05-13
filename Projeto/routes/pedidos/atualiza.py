from flask import Blueprint, render_template, request
import mysql.connector

atualizap_route = Blueprint('atualizap', __name__)

@atualizap_route.route('/pedido_atualizado', methods=['POST'])
def atualizar_pedido():
    id = request.form['spedido']
    status = request.form['astatus']
    observa = request.form['observa']
    
    if status == 1:status="Pedido em Aberto" 
    else: status ="Pedido Entregue"

    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"""UPDATE pedidos SET
                 status='{status}', observa='{observa}'
                WHERE id='{id}'""" )
        cursor= conexao.cursor()
        cursor.execute(comando)
        conexao.commit()       

        comando = ("SELECT * FROM clientes ORDER BY nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        for i in retorno:
            clie = i[1]
            clientes.append(clie)
        

        if conexao.is_connected():
            cursor.close()
            conexao.close()
            return render_template('pedidos/pedidos_atualiza.html', clientes=clientes)
# @atualiza_route.route('/home1')
# def home1():
#     return render_template('home.html')

# @atualiza_route.route('/home1')
# def home():
#     return render_template('home.html')

# @atualiza_route.route('/atualiza')
# def atualizar():
#     return render_template('pedidos/pedidos_atualiza.html')

# @atualiza_route.route('/consulta')
# def consultar():
#     return render_template('pedidos/pedidos_consulta.html')

# @atualiza_route.route('/exclui')
# def excluir():
#     return render_template('pedidos/pedidos_exclui.html')
