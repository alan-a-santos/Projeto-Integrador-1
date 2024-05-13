from flask import Blueprint, render_template, request
import mysql.connector

excluip_route = Blueprint('excluip', __name__)

@excluip_route.route('/exclui_pedido', methods=["POST"])
def excluirp(): 
    id = request.form['spedido']
    print(id)
    
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
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

