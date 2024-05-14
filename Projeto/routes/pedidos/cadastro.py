from flask import Blueprint, render_template, request
import mysql.connector
from datetime import date
from database import acesso

cadastrop_route = Blueprint('cadastrop', __name__)

@cadastrop_route.route('/cadastro_pedido', methods=['post'])
def  cadastrar_cliente():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
        idcliente = request.form['id']
        entrega = request.form['entrega']
        dentrega = request.form['dentrega']
        quant = request.form['quant']
        descricao = request.form['descricao']
        observa = request.form['observa']

        if entrega == 1:entrega="No Endereço" 
        else: entrega ="Retirada pelo Cliente"

        prato ={"0": 'Marmita Fitness - Pequena', '1': 'Marmita Fitness - Média','2': 'Marmita Fitness - Grande', '3': 'Marmita Fitness - Mista'}
        descricao = prato[descricao]

        comando = (f"INSERT INTO pedidos (id,idcliente,entrega,dentrega,quantidade,descricao,observa,cadastro,status) VALUES (default,'{idcliente}','{entrega}','{dentrega}','{quant}','{descricao}','{observa}','{date.today()}','Pedido em Aberto');")
        cursor= conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        retorno = cursor.fetchall()
        
        comando = ("SELECT * FROM clientes order by nome")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno1 = cursor.fetchall()
        conexao.commit()
        clientes=[]
        
        for i in retorno1:
            h =i[1]
            clientes.append(h)
  
    if conexao.is_connected():
        cursor.close()
        conexao.close()
    
    return render_template('pedidos/pedidos_cadastro.html', clientes=clientes)
