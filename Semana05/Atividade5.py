idades = []
posicoes = []
salarios = []

soma_salarios = 0
cont_atacantes_ate_10k = 0
cont_atacantes = 0
cont_defensores = 0

for i in range(10):
    print(f"\nJogador {i+1}:")
    
    idade = int(input("Idade: "))
    posicao = input("Posição (A para atacante / D para defensor): ").upper()
    salario = float(input("Salário: "))
    
    idades.append(idade)
    posicoes.append(posicao)
    salarios.append(salario)
    
    soma_salarios += salario
    
    if posicao == 'A':
        cont_atacantes += 1
        if salario <= 10000:
            cont_atacantes_ate_10k += 1
    elif posicao == 'D':
        cont_defensores += 1

media_salarios = soma_salarios / 10
mais_novo = min(idades)
mais_velho = max(idades)

print("\nRESULTADOS ")
print("Média dos salários: R$ {media_salarios:.2f}")
print("Jogador mais novo: {mais_novo} anos")
print("Jogador mais velho: {mais_velho} anos")
print("Atacantes com salário até R$10.000,00: {cont_atacantes_ate_10k}")
print("Quantidade de atacantes: {cont_atacantes}")
print("Quantidade de defensores: {cont_defensores}")
