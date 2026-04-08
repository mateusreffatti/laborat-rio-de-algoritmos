morango = float(input("Digite a quantidade de morangos (Kg): "))
maçã = float(input("Digite a quantidade de maçãs (Kg): "))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

if maçã <= 5:
    preco_maçã = maçã * 1.80
else:
    preco_maçã = maçã * 1.50

total = preco_morango + preco_maçã
peso_total = morango + maçã

if peso_total > 8 or total > 25:
    total = total * 0.9  

print("Valor a pagar: R$ (total:.2f)")
