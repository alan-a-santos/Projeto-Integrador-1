from flask import Blueprint, render_template, request
import mysql.connector
from database import acesso
pedido_route = Blueprint('pedido', __name__)

@pedido_route.route('/cadastrop')
def incluir():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        
        for i in retorno:
            h =i[1]
            clientes.append(h)
  
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('pedidos/pedidos_cadastro.html', clientes=clientes)
    

@pedido_route.route('/consultap')
def consultar():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)

    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        
        for i in retorno:
            h =i[1]
            clientes.append(h)
  
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            return render_template('pedidos/pedidos_consulta.html', clientes=clientes)
    #return render_template('pedidos/pedidos_consulta.html')

@pedido_route.route('/atualizap')
def atualizap():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        
        for i in retorno:
            h =i[1]
            clientes.append(h)
  
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            return render_template('pedidos/pedidos_atualiza.html', clientes=clientes)

@pedido_route.route('/excluip')
def excluir():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        
        for i in retorno:
            h =i[1]
            clientes.append(h)
  
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            return render_template('pedidos/pedidos_exclui.html', clientes=clientes)
