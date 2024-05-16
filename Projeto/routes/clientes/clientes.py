from flask import Blueprint, render_template
import mysql.connector
import json
from database import acesso

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/cadastro')
def cadastro():
    return render_template('clientes/clientes_cadastro.html')

@cliente_route.route('/consulta')
def consulta():
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
    return render_template('clientes/clientes_consulta.html', clientes=clientes)

@cliente_route.route('/atualiza')
def atualiza():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        lista =[]
        for i in retorno:
            clie = i[1]
            clientes.append(clie)
       
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('clientes/clientes_atualiza.html',clientes=clientes)

@cliente_route.route('/exclui')
def exclui():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        lista =[]
        for i in retorno:
            clie = i[1]
            clientes.append(clie)

        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('clientes/clientes_exclui.html',clientes=clientes)

@cliente_route.route('/home')
def home():
    return render_template('home.html')






