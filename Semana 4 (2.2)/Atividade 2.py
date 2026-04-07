f1 = float(input("Digite a primeira força: "))
f2 = float(input("Digite a segunda força: "))
f3 = float(input("Digite a terceira força: "))

if (f1 + f2 > f3) and (f1 + f3 > f2) and (f2 + f3 > f1):
    print("\nHá equilíbrio entre as forças.")

    if f1 == f2 == f3:
        print("Tipo: Simétrico")
    elif f1 == f2 or f1 == f3 or f2 == f3:
        print("Tipo: Parcialmente simétrico")
    else:
        print("Tipo: Assimétrico")
else:
    print("\nNão há equilíbrio entre as forças.")
