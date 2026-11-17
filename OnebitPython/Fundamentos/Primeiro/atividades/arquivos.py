import json
import csv
"""arquivo = open("ola.txt")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()"""

"""with open("ola.txt" "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)"""

with open("ola.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("ATT do conteudo\n")

"""def contar_linhas(arquivo):
    #Conta linhas de arquivo.
    with open(arquivo) as f:
        return len(f.readlines())
"""
"""def filtrar_palavras(arquivo, palavra):
    #Filtra linhas que contém palavra.
    resultados = []
    with open(arquivo) as f:
        for linha in f:
            if palavra.lower() in linha.lower():
                resultados.append(linha.strip())
    return resultados

print(contar_linhas("dados.txt"))
print(filtrar_palavras("dados.txt", "python"))"""

with open("nome.json", "w", encoding="utf-8") as arquivo:
    dados = {
        "nome": "joão",
        "idade": 25,
        "skills": ["python", "javascript"]
    }

    json.dump(dados, arquivo, indent=4, ensure_ascii=False) # dumps para transformar em string, dump para jogar num arquivo

with open("nome.json", "r", encoding="utf-8") as arquivo:
    usuario = json.load(arquivo)
    print(usuario)

with open("nomes.csv", "w", encoding="utf-8") as arquivo:
    dados = [
        ["nome", "idade", "cidade"],
        ["joão", 22, "SP"],
        ["maria", 28, "RJ"],
        ["carlos", 21, "MG"]
    ]

    writer = csv.writer(arquivo)
    writer.writerows(dados)

with open("nomes.csv", "r", encoding="utf-8") as arquivo:
    """reader = csv.reader(arquivo)

    for linha in reader:
        print(linha)"""
    reader = csv.DictReader(arquivo)

    for elemento in reader:
        print(elemento)
