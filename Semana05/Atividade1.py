capacidade = 100
vendidos = 0

while True:
    print("\n--- MENU ---")
    print("1 - Vender ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if vendidos < capacidade:
            vendidos += 1
            print("Ingresso vendido com sucesso!")
        else:
            print("Estádio lotado! Não há ingressos disponíveis.")

    elif opcao == "2":
        extras = int(input("Quantos ingressos extras deseja adicionar? "))
        capacidade += extras
        print(f"Nova capacidade: (capacidade)")

    elif opcao == "3":
        disponiveis = capacidade - vendidos
        print("Ingressos disponíveis: (disponiveis)")

    elif opcao == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")
