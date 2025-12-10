"""
API de Bloco de Notas usando Tornado
Instalar: pip install tornado
Executar: python tornado_app.py
"""

import tornado.ioloop
import tornado.web
import json
from datetime import datetime

# Banco de dados em memória
notas_db = []
contador_id = 1

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"mensagem": "API de Bloco de Notas com Tornado"})

class NotasHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"notas": notas_db})
    
    def post(self):
        global contador_id
        dados = json.loads(self.request.body)
        
        nota = {
            "id": contador_id,
            "titulo": dados.get("titulo"),
            "conteudo": dados.get("conteudo"),
            "data_criacao": datetime.now().isoformat()
        }
        
        notas_db.append(nota)
        contador_id += 1
        
        self.set_status(201)
        self.write(nota)

class NotaHandler(tornado.web.RequestHandler):
    def get(self, nota_id):
        nota_id = int(nota_id)
        for nota in notas_db:
            if nota["id"] == nota_id:
                self.write(nota)
                return
        self.set_status(404)
        self.write({"erro": "Nota não encontrada"})
    
    def put(self, nota_id):
        nota_id = int(nota_id)
        dados = json.loads(self.request.body)
        
        for i, nota in enumerate(notas_db):
            if nota["id"] == nota_id:
                notas_db[i].update({
                    "titulo": dados.get("titulo", nota["titulo"]),
                    "conteudo": dados.get("conteudo", nota["conteudo"])
                })
                self.write(notas_db[i])
                return
        
        self.set_status(404)
        self.write({"erro": "Nota não encontrada"})
    
    def delete(self, nota_id):
        nota_id = int(nota_id)
        for i, nota in enumerate(notas_db):
            if nota["id"] == nota_id:
                notas_db.pop(i)
                self.set_status(204)
                return
        
        self.set_status(404)
        self.write({"erro": "Nota não encontrada"})

def make_app():
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/notas", NotasHandler),
        (r"/notas/([0-9]+)", NotaHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Servidor rodando na porta 8888")
    tornado.ioloop.IOLoop.current().start()
