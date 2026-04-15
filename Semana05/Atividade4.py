tempos = 

for i in range(7):
    tempo = float(input(f"Digite o tempo do corredor {i+1} (em minutos): "))
    tempos.append(tempo)

# Cálculo da média
media = sum(tempos) / len(tempos)

menos_30 = 0
entre_30_60 = 0

for tempo in tempos:
    if tempo < 30:
        menos_30 += 1
    elif 30 <= tempo <= 60:
        entre_30_60 += 1

porcentagem_30_60 = (entre_30_60 / 7) * 100

print("\nTempo médio: (media:.2f) minutos")
print("Corredores com tempo menor que 30 minutos: {menos_30}")
print("Porcentagem entre 30 e 60 minutos: (porcentagem_30_60:.2f)%")
