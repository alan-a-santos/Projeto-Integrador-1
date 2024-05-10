from flask import Blueprint, render_template, request
import mysql.connector
exclui_route = Blueprint('exclui', __name__)

@exclui_route.route('/cliente_excluido' ,methods=['post'])
def excluir_cliente():
    nome = request.form['nome']
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f""" DELETE from clientes WHERE nome='{nome}'""" )
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
            return render_template('clientes/clientes_exclui.html', clientes=clientes)
