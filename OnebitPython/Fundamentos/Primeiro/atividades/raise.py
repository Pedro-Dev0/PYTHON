def definir_idade(idade):
    if idade < 0:
        raise ValueError("idade não pode ser negativa")
    elif idade > 140:
        raise ValueError("Idade deve ser realista")
    return idade 

try:
    print(definir_idade(-5))
except ValueError as error:
    print(f"erro: {error}")