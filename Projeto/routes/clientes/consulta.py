from flask import Blueprint, render_template,request, jsonify
import mysql.connector
from database import acesso
import json
consulta_route = Blueprint('consulta', __name__)

@consulta_route.route('/consulta', methods=['post'])
def dados():
    cliente = request.json.get('cliente')
  
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
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


