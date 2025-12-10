# APIs Python - Exemplos de Frameworks

Este projeto contém exemplos de APIs RESTful para um sistema de bloco de notas (CRUD) implementado com diferentes frameworks Python.

## 📚 Frameworks Implementados

1. **FastAPI** - `fastapi_app.py`
2. **Flask** - `flask_app.py`
3. **Django REST Framework** - `django_rest_app.py`
4. **Sanic** - `sanic_app.py`
5. **Tornado** - `tornado_app.py`
6. **Falcon** - `falcon_app.py`
7. **Bottle** - `bottle_app.py`

## 🚀 Como Executar

### Instalar Dependências

```bash
pip install -r requirements.txt
```

### Executar Cada Framework

**FastAPI:**

```bash
uvicorn fastapi_app:app --reload --port 8000
```

**Flask:**

```bash
python flask_app.py
# Roda na porta 5000
```

**Sanic:**

```bash
python sanic_app.py
# Roda na porta 8000
```

**Tornado:**

```bash
python tornado_app.py
# Roda na porta 8888
```

**Falcon:**

```bash
uvicorn falcon_app:app --port 8000
```

**Bottle:**

```bash
python bottle_app.py
# Roda na porta 8080
```

## 📝 Endpoints Disponíveis

Todos os frameworks implementam os mesmos endpoints:

- `GET /` - Mensagem de boas-vindas
- `POST /notas` - Criar nova nota
- `GET /notas` - Listar todas as notas
- `GET /notas/{id}` - Obter nota específica
- `PUT /notas/{id}` - Atualizar nota
- `DELETE /notas/{id}` - Deletar nota

## 🧪 Testar a API

### Criar uma nota:

```bash
curl -X POST http://localhost:8000/notas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Minha Nota", "conteudo": "Conteúdo da nota"}'
```

### Listar notas:

```bash
curl http://localhost:8000/notas
```

### Obter nota específica:

```bash
curl http://localhost:8000/notas/1
```

### Atualizar nota:

```bash
curl -X PUT http://localhost:8000/notas/1 \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Nota Atualizada", "conteudo": "Novo conteúdo"}'
```

### Deletar nota:

```bash
curl -X DELETE http://localhost:8000/notas/1
```

## 📊 Comparação dos Frameworks

| Framework | Performance | Facilidade | Async | Comunidade |
| --------- | ----------- | ---------- | ----- | ---------- |
| FastAPI   | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐⭐ | ✅    | Grande     |
| Flask     | ⭐⭐⭐      | ⭐⭐⭐⭐⭐ | ❌    | Enorme     |
| Django RF | ⭐⭐⭐      | ⭐⭐⭐     | ⚠️    | Enorme     |
| Sanic     | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐   | ✅    | Média      |
| Tornado   | ⭐⭐⭐⭐    | ⭐⭐⭐     | ✅    | Média      |
| Falcon    | ⭐⭐⭐⭐⭐  | ⭐⭐⭐     | ✅    | Pequena    |
| Bottle    | ⭐⭐⭐      | ⭐⭐⭐⭐⭐ | ❌    | Pequena    |

## 🎯 Quando Usar Cada Framework

- **FastAPI**: APIs modernas, documentação automática, validação de dados
- **Flask**: Projetos pequenos e médios, prototipagem rápida
- **Django REST**: Aplicações complexas com admin, ORM robusto
- **Sanic**: Alta performance com suporte async
- **Tornado**: WebSockets, aplicações real-time
- **Falcon**: APIs minimalistas de alta performance
- **Bottle**: Microserviços simples, um único arquivo

## 📦 Estrutura de Dados

```json
{
  "id": 1,
  "titulo": "Título da Nota",
  "conteudo": "Conteúdo da nota aqui...",
  "data_criacao": "2025-12-10T10:30:00"
}
```

## 🔧 Observações

- Todos os exemplos usam banco de dados em memória para simplicidade
- Para produção, implemente persistência com banco de dados real
- Django REST Framework requer configuração adicional de projeto
- Adicione autenticação e autorização para uso em produção
# python-rest-api-examples
