from flask import Blueprint, render_template, request
import mysql.connector
from database import acesso

atualizap_route = Blueprint('atualizap', __name__)

@atualizap_route.route('/pedido_atualizado', methods=['POST'])
def atualizar_pedido():
    id = request.form['spedido']
    status = request.form['astatus']
    observa = request.form['observa']
    print(status)
    if status == "2":
        status="Pedido Entregue" 
    else: 
        status ="Pedido em Aberto"
    print(status)
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
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
