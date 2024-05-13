from flask import Blueprint, render_template, request, jsonify
import mysql.connector
import json

consultap_route = Blueprint('consultap', __name__)

@consultap_route.route('/consultap', methods=['post'])
def consulta():
    cliente = request.json.get('cliente')
   
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"SELECT * FROM clientes WHERE nome = '{cliente}' " )
        cursor= conexao.cursor(dictionary=True)
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()              
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    
    return jsonify(retorno) 
   
@consultap_route.route('/consultap1', methods=['post'])  
def consultap():
    cod = request.json.get('cod')
    sta = request.json.get('sta')
    
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"SELECT cadastro, id FROM pedidos WHERE idcliente = '{cod}' and status ='{sta}' ")
        cursor= conexao.cursor(dictionary=True)
        cursor.execute(comando)
        resposta = cursor.fetchall()
      
        conexao.commit()              
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    
    return jsonify(resposta)    
    
@consultap_route.route('/consultap2', methods=['post'])
def consultap2():
    pedido = request.json.get('pedido')
   
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"SELECT * FROM pedidos WHERE id = '{pedido}' " )
        cursor= conexao.cursor(dictionary=True)
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()              
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    
    return jsonify(retorno) 
 