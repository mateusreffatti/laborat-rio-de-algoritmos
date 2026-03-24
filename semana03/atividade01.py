Salário do funcionário
horas = float(input("Digite o total de horas trabalhadas no mês: "))
salario = horas * 35

if salario < 1000:
   salario += 300

print(f"Salário final: R$ (salario:.2f)")
