from flask import Blueprint, render_template, request
import mysql.connector
from datetime import date
from database import acesso

cadastro_route = Blueprint('cadastro', __name__)


@cadastro_route.route('/cliente_cadastrado', methods=['post'])
def  cadastrar_cliente():
    conexao = mysql.connector.connect(host=acesso.host, database=acesso.database,user=acesso.user, password=acesso.password)
    if conexao.is_connected():
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

        comando = (f"INSERT INTO clientes (id,nome,cpf,nascimento,celular,email,instagram,cep,endereco,numero,bairro,cidade,observacao,cadastro) VALUES (default,'{nome}','{cpf}','{nascimento}','{celular}','{email}','{instagram}','{cep}','{endereco}','{num}','{bairro}','{cidade}','{observa}','{date.today()}');")
        cursor= conexao.cursor()
        cursor.execute(comando)
        conexao.commit()
        retorno = cursor.fetchall()
        
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        
    return render_template('clientes/clientes_cadastro.html')


