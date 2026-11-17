import requests
import json
from typing import Dict, Optional
from datetime import datetime

def obter_cotacoes(moeda_base: str, moedas: list) -> Optional[Dict]:
    """Obtém cotações de moedas."""
    url = f""
    
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        
        dados = resposta.json()
        taxas = {}
        
        for moeda in moedas:
            if moeda in dados["rates"]:
                taxas[moeda] = dados["rates"][moeda]
            else:
                print(f"Aviso: moeda {moeda} não encontrada")
        
        return taxas
    
    except requests.exceptions.Timeout:
        print("Erro: requésição expirou")
        return None
    except requests.exceptions.ConnectionError:
        print("Erro: conexão falhou")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e}")
        return None

def salvar_json(arquivo: str, moeda_base: str, taxas: Dict) -> None:
    """Salva cotações em JSON."""
    dados = {
        "timestamp": datetime.now().isoformat(),
        "moeda_base": moeda_base,
        "taxas": taxas
    }
    
    try:
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Arquivo '{arquivo}' criado com sucesso")
    except IOError as e:
        print(f"Erro ao escrever arquivo: {e}")

# Uso
moedas = ["USD", "EUR", "GBP"]
taxas = obter_cotacoes("BRL", moedas)

if taxas:
    salvar_json("cotacoes.json", "BRL", taxas)
    
    print("\nCotações:")
    for moeda, taxa in taxas.items():
        print(f"1 BRL = {taxa:.4f} {moeda}")