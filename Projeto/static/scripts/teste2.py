from flask import request

texto = request.form['nome']
print(texto)