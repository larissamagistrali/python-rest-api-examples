"""
API de Bloco de Notas usando Sanic
Instalar: pip install sanic
Executar: python sanic_app.py
"""

from sanic import Sanic, response
from datetime import datetime

app = Sanic("BlocoNotasAPI")

# Banco de dados em memória
notas_db = []
contador_id = 1

@app.get("/")
async def home(request):
    return response.json({"mensagem": "API de Bloco de Notas com Sanic"})

@app.post("/notas")
async def criar_nota(request):
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
    
    return response.json(nota, status=201)

@app.get("/notas")
async def listar_notas(request):
    return response.json(notas_db)

@app.get("/notas/<nota_id:int>")
async def obter_nota(request, nota_id):
    for nota in notas_db:
        if nota["id"] == nota_id:
            return response.json(nota)
    return response.json({"erro": "Nota não encontrada"}, status=404)

@app.put("/notas/<nota_id:int>")
async def atualizar_nota(request, nota_id):
    dados = request.json
    
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db[i].update({
                "titulo": dados.get("titulo", nota["titulo"]),
                "conteudo": dados.get("conteudo", nota["conteudo"])
            })
            return response.json(notas_db[i])
    
    return response.json({"erro": "Nota não encontrada"}, status=404)

@app.delete("/notas/<nota_id:int>")
async def deletar_nota(request, nota_id):
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db.pop(i)
            return response.empty(status=204)
    
    return response.json({"erro": "Nota não encontrada"}, status=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
