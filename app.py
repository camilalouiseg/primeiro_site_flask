#importando a classe Flask do framework flask, entre outros
from flask import Flask, jsonify, render_template, request
import json

#cria uma instância(objeto) da classe Flask
app = Flask(__name__)


#cria uma rota e retorna um arquivo html
@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/contatos')
def contatos():
    return render_template("contatos.html")


#a função retorna uma pagina de boas vindas html
# o texto "nome_visitante" escrito no html é igual a variavel "nome_visitante" solicitada pela função
@app.route('/visitante/<nome_visitante>')
def usuarios(nome_visitante):
    return render_template("visitante.html", nome_visitante = nome_visitante)


@app.route('/soma', methods=['POST', 'GET'])
def soma():
    # Define um valor padrão para total
    total = None
    
    # Verifica o tipo de solicitação: POST ou GET
    if request.method == 'POST':
        # Se for POST, carrega os dados JSON da solicitação
        dados = json.loads(request.data)
        # Calcula a soma dos valores fornecidos na chave 'valores'
        total = sum(dados['valores'])
    elif request.method == 'GET':
        # Se for GET, retorna uma mensagem de erro
        return jsonify({'error': 'Escolha o método POST e defina os valores'})
    
    # Retorna a soma calculada em formato JSON
    return jsonify({'soma': total})



#coloca o site no ar
#roda o arquivo diretamente, não roda se for importado
if __name__ == '__main__':
    app.run(debug=True)