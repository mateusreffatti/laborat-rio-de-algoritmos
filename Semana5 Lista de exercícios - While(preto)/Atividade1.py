reservatorio = 500  
consumo = 30        
ciclos = 0

while reservatorio >= consumo:
    reservatorio -= consumo
    ciclos += 1

print(f"Quantidade de ciclos realizados: {ciclos}")
print(f"Água restante no reservatório: {reservatorio} litros")
