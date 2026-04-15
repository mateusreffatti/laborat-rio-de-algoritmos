plantacao_a = 80000
plantacao_b = 200000

anos = 0

while plantacao_a < plantacao_b:
    plantacao_a *= 1.03
    plantacao_b *= 1.015
    anos += 1

print("A plantação A irá igualar ou ultrapassar a plantação B em anos.")
print("Plantação A: plantacao_a:.} mudas")
print("Plantação B: plantacao_b} mudas")
