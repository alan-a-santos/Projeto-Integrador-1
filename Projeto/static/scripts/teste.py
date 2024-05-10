import mysql.connector
import json
from datetime import date, datetime
import os

clie = "ALAN APARECIDO DOS SANTOS"
conexao = mysql.connector.connect(host='localhost', database='d_mais',user='root', password='aas798118')
if conexao.is_connected():
    comando = (f"SELECT * FROM clientes WHERE nome = '{clie}'" )
    comando1= ("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA= 'd_mais' AND TABLE_NAME='clientes'" )
    cursor= conexao.cursor(dictionary=True)
    cursor.execute(comando)
    retorno = cursor.fetchall()
    # cursor.execute(comando1)
    # titulo = cursor.fetchall()
  
    conexao.commit()

   
    print(retorno)

    

    #print("Conectado ao banco de dados
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Desconectado do banco de dados")