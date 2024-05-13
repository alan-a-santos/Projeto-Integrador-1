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
    print(cod,sta)
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"SELECT cadastro, id FROM pedidos WHERE idcliente = '{cod}' and status ='{sta}' ")
        cursor= conexao.cursor(dictionary=True)
        cursor.execute(comando)
        resposta = cursor.fetchall()
        print(resposta)
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
    
    
    
    # if conexao.is_connected():
    #     comando = ("SELECT * FROM clientes order by nome")
    #     cursor= conexao.cursor()
    #     cursor.execute(comando)
    #     retorno1 = cursor.fetchall()
    #     conexao.commit()
    #     clientes=[]
        
    #     for i in retorno1:
    #         h =i[1]
    #         clientes.append(h)

# @consulta_route.route('/home1')
# def home1():
#     return render_template('home.html')

# @consulta_route.route('/home1')
# def home():
#     return render_template('home.html')

# @consulta_route.route('/atualizap')
# def atualizar():
#     return render_template('pedidos/pedidos_atualiza.html')

# @consulta_route.route('/consultap')
# def consultar():
#     return render_template('pedidos/pedidos_consulta.html')

# @consulta_route.route('/excluip')
# def excluir():
#     return render_template('pedidos/pedidos_exclui.html')
