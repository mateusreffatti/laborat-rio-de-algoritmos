
valor = float(input("Digite o valor do ingresso: "))

print("\nOpções:")
print("1 - Ingresso normal")
print("2 - Estudante (50% de desconto)")
print("3 - Criança até 12 anos (paga 40%)")
print("4 - Idoso (paga 60%)")

opcao = int(input("Escolha a opção: "))

if opcao == 1:
    valor_final = valor
elif opcao == 2:
    valor_final = valor * 0.5
elif opcao == 3:
    valor_final = valor * 0.4
elif opcao == 4:
    valor_final = valor * 0.6
else:
    print("Opção inválida!")
    valor_final = None
if valor_final is not None:
    print(f"Valor a pagar: R$ {valor_final:.2f}")
