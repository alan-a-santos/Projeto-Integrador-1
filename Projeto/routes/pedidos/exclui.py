from flask import Blueprint, render_template, request
import mysql.connector
from database import acesso

excluip_route = Blueprint('excluip', __name__)

@excluip_route.route('/exclui_pedido', methods=["POST"])
def excluirp(): 
    id = request.form['spedido']
    print(id)
    
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = (f""" DELETE from pedidos WHERE id='{id}'""" )
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
            return render_template('pedidos/pedidos_exclui.html', clientes=clientes)

