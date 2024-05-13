from flask import Blueprint, render_template, request
import mysql.connector

atualiza_route = Blueprint('atualiza', __name__)

@atualiza_route.route('/cliente_atualizado', methods=['POST'])
def atualizar_cliente():
    id = request.form['id']
    nome = request.form['nome']
    cpf = request.form['cpf']
    nascimento = request.form['nascimento']
    celular = request.form['celular']
    email = request.form['email']
    instagram = request.form['instagram']
    cep = request.form['cep']
    endereco = request.form['endereco']
    num = request.form['num']
    bairro = request.form['bairro']
    cidade = request.form['cidade']
    observa = request.form['observa']

    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
    if conexao.is_connected():
        comando = (f"""UPDATE clientes SET
                nome = '{nome}' , cpf ='{cpf}', nascimento ='{nascimento}', celular = '{celular}', email='{email}', instagram='{instagram}', cep='{cep}', endereco='{endereco}', numero='{num}', bairro='{bairro}', cidade='{cidade}', observacao='{observa}'
                   WHERE id='{id}'""" )
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
            return render_template('clientes/clientes_atualiza.html', clientes=clientes)

