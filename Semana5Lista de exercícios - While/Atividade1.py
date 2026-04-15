colheitas = 

for i in range(7):
    qtd = int(input(f"Digite a quantidade colhida no dia {i+1}: "))
    colheitas.append(qtd)

total = sum(colheitas)
maior = max(colheitas)
menor = min(colheitas)

dia_maior = colheitas.index(maior) + 1
dia_menor = colheitas.index(menor) + 1

print("\n--- RESULTADOS ---")
print(f"Total colhido na semana: {total}")
print(f"Maior colheita: {maior} (dia {dia_maior})")
print(f"Menor colheita: {menor} (dia {dia_menor})")
