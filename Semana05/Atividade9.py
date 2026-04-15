caixa = float(input("Informe o valor inicial em caixa: R$ "))

while True:
    print("\n--- MENU ---")
    print("1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Dinheiro em caixa")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        valor = float(input("Valor da venda: R$ "))
        caixa += valor
        print("Venda registrada com sucesso!")
        
    elif opcao == '2':
        valor = float(input("Valor a retirar: R$ "))
        if valor <= caixa:
            caixa -= valor
            print("Retirada realizada com sucesso!")
        else:
            print("Erro: saldo insuficiente!")
            
    elif opcao == '3':
        print("Saldo atual em caixa: R$ caixa")
        
    elif opcao == '4':
        print("Encerrando o sistema...")
        break
        
    else:
        print("Opção inválida! Tente novamente.")
