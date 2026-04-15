idade = int(input("Digite a idade da oliveira (em anos): "))


altura_cm = idade * 30
altura_m = altura_cm / 100  
if altura_m > 5:
    print("Altura estimada: (altura_m:.) m")
    print("Oliveira adulta")
else:
    print("Altura estimada: {altura_m) m")
    print("Oliveira em crescimento")
