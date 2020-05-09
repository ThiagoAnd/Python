def index():
    # para repitir as funcoes quantas for necessario
    while True:
        print("\n++++++ MEMU OUTPUT ++++++++ ")
        # Entrar com opcao desejada
        opcao = input("| 1 | Listar Conteudo da Calculadora \n| 2 | Listar Conteudo da  Maquina de Vendas \n| 0 | Menu principal")
        # ifs para vereficar as qual funcao foi escolhida
        if opcao == '1':
            # try caso tenha um erro
            try:
                # open abrir arquivo
                f = open("calculadora.txt", "r")
                print(f.read())
             # tratar caso tenha erro
            except:
                print("Possivelmente esse arquivo esta vazio.\n")
        elif opcao == '2':
            try:
                f = open("compras.txt", "r")
                print(f.read())
            except:
                print("Possivelmente esse arquivo esta vazio.\n")
        elif opcao == '0':
            print("Voltando Menu Principal ....\n\n")
            break
        else:
            print("\nOpcao Invalida")