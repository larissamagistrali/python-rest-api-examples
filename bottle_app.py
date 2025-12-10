"""
API de Bloco de Notas usando Bottle
Instalar: pip install bottle
Executar: python bottle_app.py
"""

from bottle import Bottle, request, response, run
import json
from datetime import datetime

app = Bottle()

# Banco de dados em memória
notas_db = []
contador_id = 1

@app.get("/")
def home():
    return {"mensagem": "API de Bloco de Notas com Bottle"}

@app.post("/notas")
def criar_nota():
    global contador_id
    dados = request.json
    
    nota = {
        "id": contador_id,
        "titulo": dados.get("titulo"),
        "conteudo": dados.get("conteudo"),
        "data_criacao": datetime.now().isoformat()
    }
    
    notas_db.append(nota)
    contador_id += 1
    
    response.status = 201
    return nota

@app.get("/notas")
def listar_notas():
    return {"notas": notas_db}

@app.get("/notas/<nota_id:int>")
def obter_nota(nota_id):
    for nota in notas_db:
        if nota["id"] == nota_id:
            return nota
    
    response.status = 404
    return {"erro": "Nota não encontrada"}

@app.put("/notas/<nota_id:int>")
def atualizar_nota(nota_id):
    dados = request.json
    
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db[i].update({
                "titulo": dados.get("titulo", nota["titulo"]),
                "conteudo": dados.get("conteudo", nota["conteudo"])
            })
            return notas_db[i]
    
    response.status = 404
    return {"erro": "Nota não encontrada"}

@app.delete("/notas/<nota_id:int>")
def deletar_nota(nota_id):
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db.pop(i)
            response.status = 204
            return
    
    response.status = 404
    return {"erro": "Nota não encontrada"}

if __name__ == "__main__":
    run(app, host="localhost", port=8080, debug=True)
