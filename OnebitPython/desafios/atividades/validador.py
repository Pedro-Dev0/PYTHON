def validar_idade(idade: int):
    if idade != int:
        raise TypeError("A idade deve ser do tipo inteiro (int)")
    if idade < 0 or idade > 150:
        raise ValueError("Idade não pode ser negativa ou transceder o natural!")
    return f"tem {idade} anos!"

try:
    print(validar_idade("1"))
except TypeError as error:
    print(f"erro: {error}")
except ValueError as error:
    print(f"erro: {error}")

def validar_senha(senha: str):
    if len(senha) < 8:
        raise ValueError("Senha muito pequena, coloque mais caracteres")

    tem_letra = False
    for caracter in senha:
        if caracter.isalpha():
            tem_letra = True
            break
    if tem_letra == False:
        raise ValueError("A senha deve conter pelo menos uma letra")
    return senha

try:
    print(validar_senha("12313141133"))
except ValueError as error:
    print(f"erro: {error}")