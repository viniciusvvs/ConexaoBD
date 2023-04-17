import pyodbc

dados_conexao = (

"Driver={SQL Server};"
"Server=DESKTOP-8G5VGUV;"
"Database=PhytonSQL;"

) 

conexao = pyodbc.connect(dados_conexao)
print("conexão bem Sucedida")

cursor = conexao.cursor()
