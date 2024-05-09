from flask import Blueprint, render_template
import mysql.connector
import json

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/cadastro')
def cadastro():
    return render_template('clientes/clientes_cadastro.html')

@cliente_route.route('/consulta')
def consulta():
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        clientesp=[]
        niver =[]
        for i in retorno:
            n=i[3]
            h =i[1]
            print(h)
            d= n.strftime("%Y/%m/%d")
            clie = [i[0],i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]
            clientes.append(h)
            niver.append(d)
            clientesp.append(clie)

        clientesp=json.dumps(clientesp)
        niver = json.dumps(niver)

        # Cria os arquivos json
    with open("static/niver.json", "w") as arquivo:
        arquivo.write(niver)
    with open("static/clientesp.json", "w") as arquivo:
        arquivo.write(clientesp)


        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('clientes/clientes_consulta.html', clientesp=clientesp , niver=niver, clientes=clientes)

@cliente_route.route('/atualiza')
def atualiza():
    
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        lista =[]
        for i in retorno:
            clie = i[1]
            d=i
            #d = [i[0],i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]
            clientes.append(clie)
            lista.append(d)
       
            
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('clientes/clientes_atualiza.html',clientes=clientes , lista=lista)

@cliente_route.route('/exclui')
def exclui():
    
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = ("SELECT * FROM clientes")
        cursor= conexao.cursor()
        cursor.execute(comando)
        retorno = cursor.fetchall()
        conexao.commit()
        clientes=[]
        lista =[]
        for i in retorno:
            clie = i[1]
            d=i
            #d = [i[0],i[1],i[2],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]]
            clientes.append(clie)
            lista.append(d)
        
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return render_template('clientes/clientes_exclui.html',clientes=clientes , lista=lista)

@cliente_route.route('/home')
def home1():
    return render_template('home.html')






