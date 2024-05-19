from flask import Blueprint, render_template, request

acesso_route = Blueprint('acesso', __name__)

@acesso_route.route('/home' ,methods=["post"])
def home():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if usuario=='admin' and senha=="123":
        return render_template('home.html')
    else:
        return render_template('acesso.html')
    print(usuario, senha)
    pip 