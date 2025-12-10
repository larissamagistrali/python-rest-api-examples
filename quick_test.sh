#!/bin/bash

# Script para testar rapidamente todas as APIs
# Execute: bash quick_test.sh <framework>

echo "🧪 Quick Test - APIs Python"
echo "=============================="

# Instalar requests se necessário
pip show requests > /dev/null 2>&1 || pip install requests

# Framework especificado ou FastAPI por padrão
FRAMEWORK=${1:-fastapi}

case $FRAMEWORK in
  fastapi)
    echo "🚀 Testando FastAPI (porta 8000)"
    URL="http://localhost:8000"
    ;;
  flask)
    echo "🚀 Testando Flask (porta 5000)"
    URL="http://localhost:5000"
    ;;
  sanic)
    echo "🚀 Testando Sanic (porta 8000)"
    URL="http://localhost:8000"
    ;;
  tornado)
    echo "🚀 Testando Tornado (porta 8888)"
    URL="http://localhost:8888"
    ;;
  falcon)
    echo "🚀 Testando Falcon (porta 8000)"
    URL="http://localhost:8000"
    ;;
  bottle)
    echo "🚀 Testando Bottle (porta 8080)"
    URL="http://localhost:8080"
    ;;
  *)
    echo "❌ Framework inválido. Use: fastapi, flask, sanic, tornado, falcon, bottle"
    exit 1
    ;;
esac

echo ""
echo "1️⃣  Testando GET /"
curl -s "$URL/" | python3 -m json.tool
echo ""

echo "2️⃣  Criando nota"
RESPONSE=$(curl -s -X POST "$URL/notas" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Teste Bash","conteudo":"Criado via curl"}')
echo $RESPONSE | python3 -m json.tool
NOTA_ID=$(echo $RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', 1))")
echo ""

echo "3️⃣  Listando notas"
curl -s "$URL/notas" | python3 -m json.tool
echo ""

echo "4️⃣  Obtendo nota #$NOTA_ID"
curl -s "$URL/notas/$NOTA_ID" | python3 -m json.tool
echo ""

echo "5️⃣  Atualizando nota #$NOTA_ID"
curl -s -X PUT "$URL/notas/$NOTA_ID" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Nota Atualizada","conteudo":"Conteúdo modificado via bash"}' | python3 -m json.tool
echo ""

echo "6️⃣  Deletando nota #$NOTA_ID"
curl -s -X DELETE "$URL/notas/$NOTA_ID" -w "\nStatus: %{http_code}\n"
echo ""

echo "✅ Teste completo!"
