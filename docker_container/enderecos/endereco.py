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

#Vizualizar ENDEREÇOS DE TODOS CLIENTES 
@app.route('/enderecos/clientes', methods=['GET'])
@auth.login_required
def enderecos_clientes():
	try:
		conn = mysql.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select clientes.id as id, clientes.nome as Nome, enderecos.rua as Rua, enderecos.numero as Numero, enderecos.complemento as Complemento, enderecos.bairro as Bairro, enderecos.cidade as Cidade, enderecos.estado as Estado, enderecos.cep as Cep from clientes join enderecos on clientes.id = enderecos.idCliente order by Nome, Rua")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualiza os endereços de UM CLIENTE ESPECÍFICO
@app.route('/enderecos/clientes/<int:id>', methods=['GET'])
@auth.login_required
def vizu_end_clientes(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select clientes.id as id,clientes.nome as Nome, enderecos.rua as Rua, enderecos.numero as Numero, enderecos.complemento as Complemento, enderecos.bairro as Bairro, enderecos.cidade as Cidade, enderecos.estado as Estado, enderecos.cep as Cep from clientes join enderecos on clientes.id = enderecos.idCliente where id = %s", id)
		linhas = cursor.fetchall() #Retornará todas as linhas com os endereços do cliente específico. 

		if not linhas:
		    return jsonify({'status':'Cliente não possui endereço cadastrado!'}), 404
		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar todos os endereços 
@app.route('/enderecos', methods=['GET'])
@auth.login_required
def enderecos():
	try:
		conn = mysql.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT idEndereco, rua, numero, complemento, bairro, cidade, estado, cep, idCliente FROM enderecos")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar um endereço específico 
@app.route('/enderecos/<int:id>', methods=['GET'])
@auth.login_required
def vizualizar(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT idEndereco, rua, numero, complemento, bairro, cidade, estado, cep, idCliente FROM enderecos WHERE idEndereco =%s", id)
		linhas = cursor.fetchone() #Retornará apenas uma linha do banco de dados

		if not linhas:
		    return jsonify({'status':'Endereço não cadastrado!'}), 404
		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Adicionar um endereço 
@app.route('/enderecos', methods=['POST'])
@auth.login_required
def adicionar():
	try:
		json = request.json #Pegando os dados para adicionar no Banco
		rua = json['rua']
		numero = json['numero']
		complemento = json['complemento']
		bairro = json['bairro']
		cidade = json['cidade']
		estado = json['estado']
		cep = json['cep']
		idCliente = json['idCliente']
		if rua and numero and complemento and bairro and cidade and estado and cep and idCliente and request.method == 'POST':			
			sqlQuery = "INSERT INTO enderecos(rua, numero, complemento, bairro, cidade, estado, cep, idCliente) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
			dados = (rua, numero, complemento, bairro, cidade, estado, cep, idCliente)
			conn = mysql.connect() #Conexão com banco de dados
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery, dados)
			conn.commit()
			resposta = jsonify({'status':'Endereço adicionado com sucesso!'})
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Atualizar um endereço 
@app.route('/enderecos', methods=['PUT'])
@auth.login_required
def atualizar():
	try:
		json = request.json
		idEndereco = json['idEndereco']
		rua = json['rua']
		numero = json['numero']
		complemento = json['complemento']
		bairro = json['bairro']
		cidade = json['cidade']
		estado = json['estado']
		cep = json['cep']
		idCliente = json['idCliente']
		if rua and numero and complemento and bairro and cidade and estado and cep and idCliente and idEndereco and request.method == 'PUT':			
			sqlQuery = "UPDATE enderecos SET rua=%s, numero=%s, complemento=%s, bairro=%s, cidade=%s, estado=%s, cep=%s, idCliente=%s WHERE idEndereco=%s"
			dados = (rua, numero, complemento, bairro, cidade, estado, cep, idCliente, idEndereco,)
			conn = mysql.connect() #Conexão banco de dados 
			cursor = conn.cursor()
			cursor.execute(sqlQuery, dados)
			conn.commit()
			resposta = jsonify({'status':'Endereço atualizado com sucesso!'})
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		 print(e)
	finally:
		 cursor.close() 
		 conn.close()

#Deletar um endereço 
@app.route('/enderecos/<int:id>', methods=['DELETE'])
@auth.login_required
def deletar(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		sqlQuery = "SELECT * FROM enderecos where idEndereco=%s"
		cursor.execute(sqlQuery, id)
		linha = cursor.fetchone()

		if not linha:
		    return jsonify({'error':'Endereço inexistente!'}), 404

		cursor.execute("DELETE FROM enderecos WHERE idEndereco =%s", (id,))
		conn.commit()
		resposta = jsonify({'status':'Endereço deletado com sucesso!'})
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Método de verificação de senha
@auth.verify_password
def verificacao(login, senha):
	usuarios= {
 	 		'douglas':'123',
 	 		'cristhian':'321'
    }
	#Valida se o login existe
	if not (login, senha): #Se não for informado retorna false
		return False
	return usuarios.get(login) == senha #Retorna verdadeiro se for iguais

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
    app.run(debug=True, host='0.0.0.0', port=5200)