from flask import Blueprint, render_template

index_route = Blueprint('index', __name__)

@index_route.route('/')
def index():
    return render_template('index.html')

@index_route.route('/acesso')
def acesso():
    return render_template('acesso.html')