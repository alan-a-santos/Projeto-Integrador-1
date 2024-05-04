from flask import Flask, Blueprint
from routes.index import index_route
from routes.acesso import acesso_route
from routes.home import home_route
from routes.clientes.clientes import cliente_route
from routes.clientes.cadastro import  cadastro_route
# from routes.clientes.atualiza import atualiza_route
# from routes.clientes.consulta import consulta_route
# from routes.clientes.exclui import exclui_route

from routes.pedidos.clientes import pedido_route

# from routes.pedidos.atualiza import atualiza_route
# from routes.pedidos.consulta import consulta_route
# from routes.pedidos.exclui import exclui_route


app= Flask(__name__)

app.register_blueprint(index_route)
app.register_blueprint( acesso_route)
app.register_blueprint(home_route)
app.register_blueprint(cliente_route)
app.register_blueprint(cadastro_route)
app.register_blueprint(pedido_route)




#if (__name__) == "(__main__)":
app.run(debug=True)