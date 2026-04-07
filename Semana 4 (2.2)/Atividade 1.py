nome = input("Digite o nome do treinador: ")
salario = float(input("Digite o salário atual: "))
tempo = int(input("Digite o tempo de serviço (anos): "))

if tempo >= 5 and salario <= 2000:
    aumento = salario * 0.10
else:
    aumento = salario * 0.05

novo_salario = salario + aumento

print("\nNome:", nome)
print("Aumento concedido: R$ (:.2f)".format(aumento))
print("Novo salário: R$ ():.2f)".format(novo_salario))
