pessoa = {
    "nome": "João",
    "idade": 22,
    "email": "joao@cartoriopaulista.com.br",
    "endereco": {
        "rua": "rua do castor",
        "numero": 200,
        "complemento": "travessia do castor"
    }
}

print(pessoa["email"])
print(pessoa.get("nome"))
print(pessoa.items())

dado_lista = list(pessoa.items())
print(dado_lista[0])

