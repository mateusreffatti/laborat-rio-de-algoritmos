preco_unitario = 1.99

print("Loja das Oliveiras – Tabela de preços\n")

for i in range(1, 51):
    total = i * preco_unitario
    print(f"{i} muda(s) – R$ {total:.2f}")
