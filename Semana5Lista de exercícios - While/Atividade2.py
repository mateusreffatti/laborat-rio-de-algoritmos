total = int(input("Digite o total de oliveiras: "))
fileiras = int(input("Digite o número de fileiras: "))

por_fileira = total // fileiras
sobra = total % fileiras

print("\nRESULTADOS ")
print("Oliveiras por fileira: por_fileira")
print("Sobras de mudas: sobra")
