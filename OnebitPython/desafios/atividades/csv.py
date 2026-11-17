import csv 
from typing import List, Dict

def ler_csv(arquivo: str) -> List[Dict]:
    """Lê arquivo CSV e retorna lista de dicts."""
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"Erro: arquivo '{arquivo}' não encontrado")
        return []

def calcular_totais(produtos: List[Dict]) -> List[Dict]:
    """Calcula total para cada produto."""
    resultado = []
    for produto in produtos:
        try:
            preco = float(produto["preco"])
            quantidade = int(produto["quantidade"])
            total = preco * quantidade
            
            produto["total"] = total
            resultado.append(produto)
        except (ValueError, KeyError) as e:
            print(f"Erro ao processar {produto}: {e}")
    
    return resultado

def escrever_csv(arquivo: str, produtos: List[Dict]) -> None:
    """Escreve produtos em CSV."""
    if not produtos:
        print("Nenhum produto para escrever")
        return
    
    campos = ["nome", "preco", "quantidade", "total"]
    
    try:
        with open(arquivo, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(produtos)
        print(f"Arquivo '{arquivo}' criado com sucesso")
    except IOError as e:
        print(f"Erro ao escrever arquivo: {e}")

# Uso
produtos = ler_csv("produtos.csv")
produtos_com_totais = calcular_totais(produtos)
escrever_csv("produtos_totais.csv", produtos_com_totais)