"""
API de Bloco de Notas usando FastAPI
Instalar: pip install fastapi uvicorn
Executar: uvicorn fastapi_app:app --reload
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="Bloco de Notas API - FastAPI")

# Modelo de dados
class Nota(BaseModel):
    id: Optional[int] = None
    titulo: str
    conteudo: str
    data_criacao: Optional[datetime] = None

# Banco de dados em memória
notas_db = []
contador_id = 1

@app.get("/")
def home():
    return {"mensagem": "API de Bloco de Notas com FastAPI"}

@app.post("/notas", response_model=Nota, status_code=201)
def criar_nota(nota: Nota):
    global contador_id
    nota.id = contador_id
    nota.data_criacao = datetime.now()
    notas_db.append(nota.dict())
    contador_id += 1
    return nota

@app.get("/notas", response_model=List[Nota])
def listar_notas():
    return notas_db

@app.get("/notas/{nota_id}", response_model=Nota)
def obter_nota(nota_id: int):
    for nota in notas_db:
        if nota["id"] == nota_id:
            return nota
    raise HTTPException(status_code=404, detail="Nota não encontrada")

@app.put("/notas/{nota_id}", response_model=Nota)
def atualizar_nota(nota_id: int, nota_atualizada: Nota):
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            nota_atualizada.id = nota_id
            nota_atualizada.data_criacao = nota["data_criacao"]
            notas_db[i] = nota_atualizada.dict()
            return nota_atualizada
    raise HTTPException(status_code=404, detail="Nota não encontrada")

@app.delete("/notas/{nota_id}", status_code=204)
def deletar_nota(nota_id: int):
    for i, nota in enumerate(notas_db):
        if nota["id"] == nota_id:
            notas_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Nota não encontrada")
