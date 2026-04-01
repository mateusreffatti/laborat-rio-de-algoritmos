
print("Escolha o kit:")
print("1 - Kit Básico (R$100,00)")
print("2 - Kit Plus (R$120,00)")
print("3 - Kit Premium (R$150,00)")

opcao = int(input("Digite a opção desejada: "))
valor_pago = float(input("Digite o valor pago: R$ "))

if opcao == 1:
    kit = "Kit Básico"
    valor_kit = 100.0
elif opcao == 2:
    kit = "Kit Plus"
    valor_kit = 120.0
elif opcao == 3:
    kit = "Kit Premium"
    valor_kit = 150.0
else:
    print("Opção inválida!")
    valor_kit = None

if valor_kit is not None:
    if valor_pago >= valor_kit:
        troco = valor_pago - valor_kit
        print(f"\nVocê escolheu: {kit}")
        print("Pagamento realizado com sucesso!")
        print(f"Troco: R$ {troco:.2f}")
    else:
        falta = valor_kit - valor_pago
        print(f"\nValor insuficiente! Faltam R$ {falta:.2f}")
