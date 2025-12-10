"""
API de Bloco de Notas usando Falcon
Instalar: pip install falcon uvicorn
Executar: uvicorn falcon_app:app
"""

import falcon
import json
from datetime import datetime

# Banco de dados em memória
notas_db = []
contador_id = 1

class HomeResource:
    def on_get(self, req, resp):
        resp.media = {"mensagem": "API de Bloco de Notas com Falcon"}

class NotasResource:
    def on_get(self, req, resp):
        resp.media = notas_db
    
    def on_post(self, req, resp):
        global contador_id
        dados = req.media
        
        nota = {
            "id": contador_id,
            "titulo": dados.get("titulo"),
            "conteudo": dados.get("conteudo"),
            "data_criacao": datetime.now().isoformat()
        }
        
        notas_db.append(nota)
        contador_id += 1
        
        resp.status = falcon.HTTP_201
        resp.media = nota

class NotaResource:
    def on_get(self, req, resp, nota_id):
        nota_id = int(nota_id)
        for nota in notas_db:
            if nota["id"] == nota_id:
                resp.media = nota
                return
        
        resp.status = falcon.HTTP_404
        resp.media = {"erro": "Nota não encontrada"}
    
    def on_put(self, req, resp, nota_id):
        nota_id = int(nota_id)
        dados = req.media
        
        for i, nota in enumerate(notas_db):
            if nota["id"] == nota_id:
                notas_db[i].update({
                    "titulo": dados.get("titulo", nota["titulo"]),
                    "conteudo": dados.get("conteudo", nota["conteudo"])
                })
                resp.media = notas_db[i]
                return
        
        resp.status = falcon.HTTP_404
        resp.media = {"erro": "Nota não encontrada"}
    
    def on_delete(self, req, resp, nota_id):
        nota_id = int(nota_id)
        for i, nota in enumerate(notas_db):
            if nota["id"] == nota_id:
                notas_db.pop(i)
                resp.status = falcon.HTTP_204
                return
        
        resp.status = falcon.HTTP_404
        resp.media = {"erro": "Nota não encontrada"}

# Criar aplicação
app = falcon.App()

# Rotas
app.add_route("/", HomeResource())
app.add_route("/notas", NotasResource())
app.add_route("/notas/{nota_id}", NotaResource())
