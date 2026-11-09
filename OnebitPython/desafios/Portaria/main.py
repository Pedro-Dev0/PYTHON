from OnebitPython.desafios.Portaria.portaria import GerenciadorPortaria

sistema = GerenciadorPortaria()

sistema.carregar_txt("convidados.txt")

print(f"DEBUG: O sistema encontrou {len(sistema._convidados)} pessoas no TXT.")

print("\n--- SISTEMA DE PORTARIA INICIADO ---")

while True:
    comando = input("Digite o nome do convidado (ou 'sair' para fechar): ")

    if comando == "sair":
        print("Encerrando o sistema...")
        break

    resultados = sistema.buscar_convidados(comando)

    if len(resultados) == 0:
        print("Não foi encontrado nenhum resultado")
        continue

    for convidado in resultados:
        print(f"Nome: {convidado.nome}, Status: {convidado.status}, Código: {convidado.codigo}")

    codigo = input("Qual o código do convidado? ")

    for convidado in resultados:
        codigo_limpo = codigo.lower()

        if codigo_limpo == convidado.codigo.lower():

            convidado.confirmar_entrada()

            sistema.salvar_csv("relatorio_portaria.csv")

            print(f"Entrada de {convidado.nome} confirmada!")
            break

