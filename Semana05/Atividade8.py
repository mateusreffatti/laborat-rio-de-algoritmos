expresso = 0
cappuccino = 0
cha = 0

for i in range(10):
    voto = input("Digite a bebida (A-Expresso, B-Cappuccino, C-Chá): ").upper()
    
    if voto == 'A':
        expresso += 1
    elif voto == 'B':
        cappuccino += 1
    elif voto == 'C':
        cha += 1

total = 10
perc_expresso = (expresso / total) * 100
perc_cappuccino = (cappuccino / total) * 100
perc_cha = (cha / total) * 100

print("\n--- RESULTADOS ---")
print("Expresso: expresso votos (perc_expresso:.1f%)")
print("Cappuccino: cappuccino votos (perc_cappuccino:.1f%)")
print("Chá: cha votos (perc_cha:.1f%)")
