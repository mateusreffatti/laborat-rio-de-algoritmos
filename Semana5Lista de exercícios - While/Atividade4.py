soma = 0

for i in range(15):
    idade = int(input("Digite a idade do estudante {i+1}: "))
    soma += idade

media = soma / 15

if 0 <= media <= 25:
    classificacao = "turma jovem"
elif 26 <= media <= 60:
    classificacao = "turma adulta"
else:
    classificacao = "turma idosa"

print("\n--- RESULTADOS ---")
print("Média de idade: media:")
print("Classificação: classificacao")
