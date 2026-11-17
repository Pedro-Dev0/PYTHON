pedidos = [    {"id": 1, "produto": "Notebook", "quantidade": 1, "preco": 2500},
    {"id": 2, "produto": "Mouse", "quantidade": 2, "preco": 50},
    {"id": 3, "produto": "Teclado", "quantidade": 1, "preco": 120},
    {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
    {"id": 4, "produto": "Monitor", "quantidade": 1, "preco": 800},
    {"id": 0, "produto": "Outros", "quantidade": 0, "preco": 0},  # Remover
    {"id": 5, "produto": "Webcam", "quantidade": 3, "preco": 150}
]

pedidos.pop(-4)
pedidos.pop(-2)
print(pedidos)

pedido_index = int(input("informe o index do pedido que deseja: \n"))
pedido = pedidos[pedido_index]

print(f"Index do pedido {pedido_index}: {pedido['produto']} - {pedido['quantidade']}x - R${pedido['preco']} - Total: R${pedido['quantidade'] * pedido['preco']}")