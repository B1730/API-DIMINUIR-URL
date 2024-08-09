#objetivo: Fazer uma APi que diminua outra API
#erros de escrita
import pyshorteners
from flask import Flask, jsonify, request

app = Flask(__name__)
explicacao = [
    {
        "mensagem": "Use o metodo PUT na rota /diminuir  Va em Body, selecione raw, escolha JSON e digite: "
                    '{ "url_longa": "<url>" }. OBS: tire as barras ( / ) caso tenha'
    }
]
@app.route("/", methods=["GET"])
def explicação():
    return(explicacao)

@app.route("/diminuir", methods=["PUT"])
def link():
    inclui = request.get_json()
    url_longa = inclui.get('url_longa')  
    
    if not url_longa:
        return jsonify({"erro": "URL longa não fornecida."}), 400
    
    type_tiny = pyshorteners.Shortener()
    url_pequena = type_tiny.tinyurl.short(url_longa)
    
    return jsonify({"COPIE E COLE NO SEU NAVEGADOR, CUIDADO AS ASPAS. url_pequena": url_pequena})

app.run(port=5000, host='localhost', debug=True)
