"""
API de Bloco de Notas usando Flask
Instalar: pip install flask
Executar: python flask_app.py
"""

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Banco de dados em memória
notas_db = []
contador_id = 1

@app.route("/")
def home():
    return jsonify({"mensagem": "API de Bloco de Notas com Flask"})

@app.route("/notas", methods=["POST"])
def criar_nota():
    global contador_id
    dados = request.get_json()
    
    nota = {
        "id": contador_id,
        "titulo": dados.get("titulo"),
        "conteudo": dados.get("conteudo"),
        "data_criacao": datetime.now().isoformat()
    }
    
    notas_db.append(nota)
    contador_id += 1
    
    return jsonify(nota), 201

@app.route("/notas", methods=["GET"])
def listar_notas():
    return jsonify(notas_db)

@app.route("/notas/<int:nota_id>", methods=["GET"])
def obter_nota(nota_id):
    for nota in notas_db:
        if nota["id"] == nota_id:
            return jsonify(nota)
    return jsonify({"erro": "Nota não encontrada"}), 404

@app.route("/notas/<int:nota_id>", methods=["PUT"])
def atualizar_nota(nota_id):
    dados = request.get_json()
    
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db[i].update({
                "titulo": dados.get("titulo", nota["titulo"]),
                "conteudo": dados.get("conteudo", nota["conteudo"])
            })
            return jsonify(notas_db[i])
    
    return jsonify({"erro": "Nota não encontrada"}), 404

@app.route("/notas/<int:nota_id>", methods=["DELETE"])
def deletar_nota(nota_id):
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db.pop(i)
            return "", 204
    
    return jsonify({"erro": "Nota não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
