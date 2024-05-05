from flask import Blueprint, render_template, request
import mysql.connector


cadastro_route = Blueprint('cadastro', __name__)


@cadastro_route.route('/cliente_cadastrado', methods=['post'])
def  cadastrar_cliente():
    conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
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

        comando = (f"""INSERT INTO clientes (id,nome,cpf,nascimento,celular,email,instagram,cep,endereco,numero,bairro,cidade,observacao) VALUES (default,'{nome}','{cpf}','{nascimento}','{celular}','{email}','{instagram}','{cep}','{endereco}','{num}','{bairro}','{cidade}','{observa}');""")
        cursor= conexao.cursor()
        
        cursor.execute(comando)
        retorno = cursor.fetchall()
        print("conectado ao banco de dados")
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("conexao encerrada")
    return render_template('clientes/clientes_cadastro.html')

# @cadastro_route.route('/atualiza')
# def atualizar():
#     return render_template('clientes/clientes_atualiza.html')

# @cadastro_route.route('/consulta')
# def consultar():
#     return render_template('clientes/clientes_consulta.html')

# @cadastro_route.route('/exclui')
# def excluir():
#     return render_template('clientes/clientes_exclui.html')

