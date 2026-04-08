tempos = ()

for i in range(1, 8):
    tempo = float(input("Digite o tempo do corredor (em minutos): "))
    tempos.append(tempo)

media = sum(tempos) / len(tempos)

menos_30 = sum(1 for t in tempos if t < 30)
entre_30_60 = sum(1 for t in tempos if 30 <= t <= 60)

porcentagem_30_60 = (entre_30_60 / len(tempos)) * 100

print("\nTempo médio dos corredores: (media:.2f) minutos")
print("Corredores que terminaram em menos de 30 minutos: (menos_30)")
print("Porcentagem de corredores entre 30 e 60 minutos: (porcentagem_30_60:.)%")
