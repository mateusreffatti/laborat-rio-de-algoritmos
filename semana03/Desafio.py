nome = input("Digite o nome do cliente: ")
valor = float(input("Digite o valor da compra: R$ "))
forma = input("Forma de pagamento (1 - Dinheiro / 2 - Cartão): ")

if valor > 200:
   if forma == "1":
       desconto = valor * 0.15
   else:
       desconto = valor * 0.05
else:
   if forma == "1":
       desconto = valor * 0.10
   else:
       desconto = 0

valor_final = valor - desconto

print("\n--- Resultado ---")
print(f"Cliente: (nome)")
print(f"Valor original: R$ (valor:.2f)")
print(f"Valor final: R$ (valor_final:.2f)")
