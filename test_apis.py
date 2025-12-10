"""
Script de Testes para todas as APIs
Testa os endpoints de CRUD de cada framework
"""

import requests
import json
import time
from typing import Dict, List

class TestadorAPI:
    def __init__(self, base_url: str, nome_framework: str):
        self.base_url = base_url
        self.nome_framework = nome_framework
        self.resultados = []
    
    def print_titulo(self, texto: str):
        print(f"\n{'='*60}")
        print(f"  {texto}")
        print(f"{'='*60}")
    
    def print_resultado(self, metodo: str, endpoint: str, status: int, dados=None):
        cor = "\033[92m" if 200 <= status < 300 else "\033[91m"
        reset = "\033[0m"
        print(f"{cor}[{metodo}] {endpoint} - Status: {status}{reset}")
        if dados:
            print(f"Resposta: {json.dumps(dados, indent=2, ensure_ascii=False)}")
    
    def testar_home(self):
        """Testa o endpoint raiz"""
        try:
            response = requests.get(f"{self.base_url}/")
            self.print_resultado("GET", "/", response.status_code, response.json())
            return response.status_code == 200
        except Exception as e:
            print(f"❌ Erro ao testar home: {e}")
            return False
    
    def criar_nota(self, titulo: str, conteudo: str) -> Dict:
        """Cria uma nova nota"""
        try:
            dados = {"titulo": titulo, "conteudo": conteudo}
            response = requests.post(
                f"{self.base_url}/notas",
                json=dados,
                headers={"Content-Type": "application/json"}
            )
            resultado = response.json()
            self.print_resultado("POST", "/notas", response.status_code, resultado)
            return resultado
        except Exception as e:
            print(f"❌ Erro ao criar nota: {e}")
            return {}
    
    def listar_notas(self) -> List:
        """Lista todas as notas"""
        try:
            response = requests.get(f"{self.base_url}/notas")
            resultado = response.json()
            # Alguns frameworks retornam {"notas": [...]}
            if isinstance(resultado, dict) and "notas" in resultado:
                resultado = resultado["notas"]
            self.print_resultado("GET", "/notas", response.status_code, resultado)
            return resultado
        except Exception as e:
            print(f"❌ Erro ao listar notas: {e}")
            return []
    
    def obter_nota(self, nota_id: int) -> Dict:
        """Obtém uma nota específica"""
        try:
            response = requests.get(f"{self.base_url}/notas/{nota_id}")
            resultado = response.json()
            self.print_resultado("GET", f"/notas/{nota_id}", response.status_code, resultado)
            return resultado
        except Exception as e:
            print(f"❌ Erro ao obter nota: {e}")
            return {}
    
    def atualizar_nota(self, nota_id: int, titulo: str, conteudo: str) -> Dict:
        """Atualiza uma nota"""
        try:
            dados = {"titulo": titulo, "conteudo": conteudo}
            response = requests.put(
                f"{self.base_url}/notas/{nota_id}",
                json=dados,
                headers={"Content-Type": "application/json"}
            )
            resultado = response.json()
            self.print_resultado("PUT", f"/notas/{nota_id}", response.status_code, resultado)
            return resultado
        except Exception as e:
            print(f"❌ Erro ao atualizar nota: {e}")
            return {}
    
    def deletar_nota(self, nota_id: int) -> bool:
        """Deleta uma nota"""
        try:
            response = requests.delete(f"{self.base_url}/notas/{nota_id}")
            self.print_resultado("DELETE", f"/notas/{nota_id}", response.status_code)
            return response.status_code in [200, 204]
        except Exception as e:
            print(f"❌ Erro ao deletar nota: {e}")
            return False
    
    def executar_teste_completo(self):
        """Executa um teste completo de CRUD"""
        self.print_titulo(f"Testando {self.nome_framework}")
        
        # 1. Testar home
        print("\n📍 Teste 1: Home")
        if not self.testar_home():
            print(f"⚠️ API {self.nome_framework} pode não estar rodando em {self.base_url}")
            return False
        
        # 2. Criar notas
        print("\n📍 Teste 2: Criar Notas")
        nota1 = self.criar_nota("Minha primeira nota", "Este é o conteúdo da primeira nota")
        time.sleep(0.2)
        nota2 = self.criar_nota("Segunda nota", "Mais um conteúdo de teste")
        time.sleep(0.2)
        nota3 = self.criar_nota("Terceira nota", "Conteúdo da terceira nota")
        
        if not nota1:
            print("❌ Falha ao criar notas")
            return False
        
        # 3. Listar notas
        print("\n📍 Teste 3: Listar Todas as Notas")
        notas = self.listar_notas()
        print(f"✅ Total de notas: {len(notas)}")
        
        # 4. Obter nota específica
        print("\n📍 Teste 4: Obter Nota Específica")
        nota_id = nota1.get("id", 1)
        self.obter_nota(nota_id)
        
        # 5. Atualizar nota
        print("\n📍 Teste 5: Atualizar Nota")
        self.atualizar_nota(nota_id, "Nota Atualizada", "Conteúdo foi modificado!")
        
        # 6. Verificar atualização
        print("\n📍 Teste 6: Verificar Atualização")
        self.obter_nota(nota_id)
        
        # 7. Deletar nota
        print("\n📍 Teste 7: Deletar Nota")
        self.deletar_nota(nota_id)
        
        # 8. Verificar listagem após delete
        print("\n📍 Teste 8: Listar Após Delete")
        notas_final = self.listar_notas()
        print(f"✅ Total de notas após delete: {len(notas_final)}")
        
        print(f"\n✅ Teste completo do {self.nome_framework} finalizado!")
        return True


def main():
    """Função principal para testar todas as APIs"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║     TESTADOR DE APIs - Bloco de Notas CRUD               ║
    ║     Teste todos os frameworks Python                      ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Configuração dos frameworks
    frameworks = {
        "FastAPI": {"url": "http://localhost:8000", "comando": "uvicorn fastapi_app:app"},
        "Flask": {"url": "http://localhost:5000", "comando": "python flask_app.py"},
        "Sanic": {"url": "http://localhost:8000", "comando": "python sanic_app.py"},
        "Tornado": {"url": "http://localhost:8888", "comando": "python tornado_app.py"},
        "Falcon": {"url": "http://localhost:8000", "comando": "uvicorn falcon_app:app"},
        "Bottle": {"url": "http://localhost:8080", "comando": "python bottle_app.py"},
    }
    
    print("\n⚠️  IMPORTANTE: Certifique-se de que pelo menos uma API está rodando!")
    print("\nPara iniciar uma API, execute em outro terminal:")
    for nome, config in frameworks.items():
        print(f"  • {nome}: {config['comando']}")
    
    print("\n" + "="*60)
    input("Pressione ENTER quando a API estiver rodando...")
    
    # Menu de seleção
    print("\n" + "="*60)
    print("Escolha o framework para testar:")
    opcoes = list(frameworks.keys())
    for i, nome in enumerate(opcoes, 1):
        print(f"  {i}. {nome} ({frameworks[nome]['url']})")
    print(f"  {len(opcoes)+1}. Testar todos (sequencialmente)")
    print(f"  0. Sair")
    
    escolha = input("\nDigite o número da opção: ").strip()
    
    if escolha == "0":
        print("👋 Até logo!")
        return
    
    if escolha == str(len(opcoes)+1):
        # Testar todos
        for nome, config in frameworks.items():
            testador = TestadorAPI(config["url"], nome)
            try:
                testador.executar_teste_completo()
                time.sleep(1)
            except Exception as e:
                print(f"❌ Erro ao testar {nome}: {e}")
                print("⏭️  Pulando para o próximo...\n")
    elif escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
        # Testar um específico
        nome = opcoes[int(escolha)-1]
        config = frameworks[nome]
        testador = TestadorAPI(config["url"], nome)
        testador.executar_teste_completo()
    else:
        print("❌ Opção inválida!")
    
    print("\n" + "="*60)
    print("✅ Testes finalizados!")
    print("="*60)


if __name__ == "__main__":
    main()
