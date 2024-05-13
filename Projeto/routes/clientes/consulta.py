from flask import Blueprint, render_template,request, jsonify
import mysql.connector
import json
consulta_route = Blueprint('consulta', __name__)

@consulta_route.route('/consulta', methods=['post'])
def dados():
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


