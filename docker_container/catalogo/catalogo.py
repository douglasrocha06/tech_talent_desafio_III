import pymysql
from app import app2
from config import mysql2
from flask import jsonify
from flask import flash, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@app2.route('/')
def welcome():
    return 'Sejam Bem-Vindos!'

#Vizualizar TODOS OS PRODUTOS
@app2.route('/catalogo', methods=['GET'])
@auth.login_required
def catalogo():
	try:
		conn = mysql2.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id_produtos, produtos, preco, estado, qtd_estoque, tamanho, genero FROM catalogo")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar UM PRODUTO ESPECÍFICO
@app2.route('/catalogo/<int:id>', methods=['GET'])
@auth.login_required
def vizualizar_prod(id):
	try:
		conn = mysql2.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id_produtos, produtos, preco, estado, qtd_estoque, tamanho, genero FROM catalogo WHERE id_produtos =%s", id)
		linhas = cursor.fetchone() #Retornará apenas uma linha do banco de dados 

		if not linhas:
		    return jsonify({'status':'Produto não cadastrado!'}), 404

		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar produtos Disponível
@app2.route('/catalogo/ativo', methods=['GET'])
@auth.login_required
def catalogo_ativo():
	try:
		conn = mysql2.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select * from catalogo where estado = 'Disponível'")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar produtos Indisponível
@app2.route('/catalogo/inativo', methods=['GET'])
@auth.login_required
def catalogo_inativo():
	try:
		conn = mysql2.connect() 
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select * from catalogo where estado = 'Indisponível'")
		linha = cursor.fetchall() #Retornará todas as linhas do banco de dados 
		resposta = jsonify(linha) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar TODAS AS VENDAS
@app2.route('/catalogo/vendas', methods=['GET'])
@auth.login_required
def vendas_prod():
	try:
		conn = mysql2.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select catalogo.id_produtos as id,catalogo.produtos as Produtos, catalogo.preco as Preço, catalogo.qtd_estoque as Qtde_Estoque, catalogo.tamanho as Tamanho, catalogo.genero as Genero, vendas.qtd_venda as Qtde_Venda, date_format(vendas.data_venda, GET_FORMAT(DATE, 'EUR')) as 'Data_Venda' from catalogo join vendas on catalogo.id_produtos = vendas.id_venda order by data_venda")
		linhas = cursor.fetchall() #Retornará apenas uma linha do banco de dados 
		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Vizualizar UMA VENDA ESPECÍFICA
@app2.route('/catalogo/vendas/<int:id>', methods=['GET'])
@auth.login_required
def vizu_venda_prod(id):
	try:
		conn = mysql2.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("select catalogo.id_produtos as id,catalogo.produtos as Produtos,catalogo.preco as Preço, catalogo.qtd_estoque as Qtde_Estoque,catalogo.tamanho as Tamanho,catalogo.genero as Genero,vendas.qtd_venda as Qtde_Venda, date_format(vendas.data_venda, GET_FORMAT(DATE, 'EUR')) as 'Data_Venda' from catalogo join vendas on catalogo.id_produtos = vendas.id_produtos where catalogo.id_produtos = %s order by data_venda", id)
		linhas = cursor.fetchall() #Retornará apenas uma linha do banco de dados 
		if not linhas:
		    return jsonify({'status':'Venda inexistente!'}), 404
		
		resposta = jsonify(linhas) #Formata em JSON
		resposta.status_code = 200
		return resposta
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Adicionar UM PRODUTO 
@app2.route('/catalogo', methods=['POST'])
@auth.login_required
def adicionar_prod():
	try:
		json = request.json #Pegando os dados para adicionar no Banco
		produtos = json['produtos']
		preco = json['preco']
		estado = json['estado']
		qtd_estoque = json['qtd_estoque']
		tamanho = json['tamanho']
		genero = json['genero']
		if produtos and preco and estado and qtd_estoque and tamanho and genero and request.method == 'POST':
			sqlQuery = "INSERT INTO catalogo(produtos, preco, estado, qtd_estoque, tamanho, genero) VALUES(%s, %s, %s, %s, %s, %s)"
			dados = (produtos, preco, estado, qtd_estoque, tamanho, genero)
			conn = mysql2.connect() #Conexão com banco de dados
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			cursor.execute(sqlQuery, dados)
			conn.commit()
			resposta = jsonify({'status':'Produto cadastrado com sucesso!'})
			resposta.status_code = 200
			return resposta
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#Atualizar UM PRODUTO 
@app2.route('/catalogo', methods=['PUT'])
@auth.login_required
def atualizar_prod():
	try:
		json = request.json
		id_produtos = json['id_produtos']
		produtos = json['produtos']
		preco = json['preco']
		estado = json['estado']
		qtd_estoque = json['qtd_estoque']
		tamanho = json['tamanho']
		genero = json['genero']
		if produtos and preco and estado and qtd_estoque and tamanho and genero and id_produtos and request.method == 'PUT':
			sqlQuery = "UPDATE catalogo SET produtos=%s, preco=%s, estado=%s, qtd_estoque=%s, tamanho=%s, genero=%s WHERE id_produtos=%s"
			dados = (produtos, preco, estado, qtd_estoque, tamanho, genero, id_produtos)
			conn = mysql2.connect() #Conexão banco de dados 
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

#Método de verificação de senha
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
@app2.errorhandler(404)
def not_found(error=None):
    messagem = {
        'status': 404,
        'mensagem': 'Registro não encontrado: ' + request.url,
    }
    respone = jsonify(messagem)
    respone.status_code = 404
    return respone
		
if __name__ == "__main__":
    app2.run(debug=True, host='0.0.0.0', port=5300)