
positivas = 0

resposta = input("Você treinou regularmente nas últimas semanas? (Sim/Não): ")
if resposta.lower() == "sim":
    positivas += 1

resposta = input("Participou de treinos longos (acima de 10 km)? (Sim/Não): ")
if resposta.lower() == "sim":
    positivas += 1

resposta = input("Seguiu uma dieta especial para a corrida? (Sim/Não): ")
if resposta.lower() == "sim":
    positivas += 1

resposta = input("Já competiu em provas oficiais neste ano? (Sim/Não): ")
if resposta.lower() == "sim":
    positivas += 1

resposta = input("Conta com acompanhamento de treinador ou equipe? (Sim/Não): ")
if resposta.lower() == "sim":
    positivas += 1

if positivas == 5:
    classificacao = "Atleta de Elite (pronto para o pódio!)"
elif positivas >= 3:
    classificacao = "Atleta Competitivo (tem boas chances de se destacar)"
elif positivas == 2:
    classificacao = "Participante Casual (ainda precisa de mais treino)"
else:
    classificacao = "Não Preparado (talvez seja melhor assistir da arquibancada este ano)"

print("\nTotal de respostas positivas: (positivas)")
print("Classificação: (classificacao)")
