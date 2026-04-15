
while True:
    idade = int(input("Digite a idade (0 a 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade inválida! Tente novamente.")

while True:
    salario = float(input("Digite o salário (maior que 0): "))
    if salario > 0:
        break
    else:
        print("Salário inválido! Tente novamente.")

while True:
    sexo = input("Digite o sexo (f/m): ").lower()
    if sexo in ['f', 'm']:
        break
    else:
        print("Sexo inválido! Tente novamente.")

while True:
    estado_civil = input("Digite o estado civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Tente novamente.")

print("\n--- DADOS VÁLIDOS ---")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
