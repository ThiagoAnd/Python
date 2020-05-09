#Faco um while em que tenho um menu que faz um import de cada arquivo python e faz a chamada da funcao index de cada um para a opcao escolhida
while True:
    print("\n++++++ MEMU PRINCIPAL ++++++++ ")
    opcao = input("| 1 | Calculadora \n| 2 | Maquina de Vendas \n| 3 | Output \n| 0 | Sair")

    if opcao == '1':
        print("Executando Calculadora ....\n\n")
        import calculadora
        calculadora.index()
    elif opcao == '2':
        print(" Executando Maquina de Vendas ....\n\n")
        import vendas
        vendas.index()
    elif opcao == '3':
        print("output ....\n\n")
        import output
        output.index()
    elif opcao == '0':
        print("Saindo ....\n\n")
        break
    else:
        print("\nOpcao Invalida")