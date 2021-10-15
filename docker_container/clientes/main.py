import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@app.route('/')
def welcome():
    return 'Sejam Bem-Vindos!'

#Vizualizar todos os clientes
@app.route('/clientes', methods=['GET'])
@auth.login_required
def clientes():
	try:
		conn = mysql.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, nome, cpf, date_format(nascimento, GET_FORMAT(DATE,'EUR')) as 'nascimento', email FROM clientes")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		return jsonify({"error":f"{e}"})
	finally:
		cursor.close() 
		conn.close()

#Vizualizar um cliente específico 
@app.route('/clientes/<int:id>', methods=['GET'])
@auth.login_required
def vizualizar_cli(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id, nome, cpf, date_format(nascimento, GET_FORMAT(DATE,'EUR')) as 'nascimento', email FROM clientes WHERE id =%s", id)
		linhas = cursor.fetchone() #Retornará apenas uma linha do banco de dados 

		if not linhas:
		    return jsonify({'status':'Cliente não cadastrado!'}), 404

		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Adicionar um cliente 
@app.route('/clientes', methods=['POST'])
@auth.login_required
def adicionar_cli():
	try:
		json = request.json #Pegando os dados para adicionar no Banco
		nome = json['nome']
		cpf = json['cpf']
		nascimento = json['nascimento']
		email = json['email']
		if nome and cpf and nascimento and email and request.method == 'POST':			
			sqlQuery = "INSERT INTO clientes(nome, cpf, nascimento, email) VALUES(%s, %s, %s, %s)"
			dados = (nome, cpf, nascimento, email)
			conn = mysql.connect() #Conexão com banco de dados
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery, dados)
			conn.commit()
			resposta = jsonify({'status':'Cliente adicionado com sucesso!'})
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Atualizar um cliente 
@app.route('/clientes', methods=['PUT'])
@auth.login_required
def atualizar_cli():
	try:
		json = request.json
		id = json['id']
		nome = json['nome']
		cpf = json['cpf']
		nascimento = json['nascimento']
		email = json['email']
		if nome and cpf and nascimento and email and id and request.method == 'PUT':
			sqlQuery = "UPDATE clientes SET nome=%s, cpf=%s, nascimento=%s, email=%s WHERE id=%s"
			dados = (nome, cpf, nascimento, email, id,)
			conn = mysql.connect() #Conexão banco de dados 
			cursor = conn.cursor()
			cursor.execute(sqlQuery, dados)
			conn.commit()
			resposta = jsonify({'status':'Dados atualizados com sucesso!'})
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		 print(e)
	finally:
		 cursor.close() 
		 conn.close()

#Deletar um cliente 
@app.route('/clientes/<int:id>', methods=['DELETE'])
@auth.login_required
def deletar_cli(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		sqlQuery = "SELECT * FROM clientes where id=%s"
		cursor.execute(sqlQuery, id)
		linha = cursor.fetchone()

		if not linha:
		    return jsonify({'status':'Cliente não cadastrado!'}), 404
		else:
			cursor.execute("DELETE FROM clientes WHERE id =%s", (id,))
			conn.commit()
			resposta = jsonify({'status':'Cliente deletado com sucesso!'})
			resposta.status_code = 200

		if not linha:
		    return jsonify({'status':'Cliente não cadastrado!'}), 404
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Método do Basic Authentication
@auth.verify_password
def verificacao(login, senha):
	usuarios= {
			'douglas':'123',
			'cristhian':'321'
	}
	#Valida se o login existe
	if not (login, senha): #Se não for igual retorna false
		return False
	return usuarios.get(login) == senha

#Caso não encontre o caminho
@app.errorhandler(404)
def not_found(error=None):
    messagem = {
        'status': 404,
        'mensagem': 'Registro nao encontrado: ' + request.url,
    }
    respone = jsonify(messagem)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5100)