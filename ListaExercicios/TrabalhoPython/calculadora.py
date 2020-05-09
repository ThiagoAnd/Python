def index():
    opcao = '1'
    resultado = 0
    num1 = 0
    num2 = 0
    print("++++++++ CALCULADORA ++++++++=")
    # repetir todas os componentes quantas vezes necessario
    while True:
        # algums ifs para valida opcao esse do menu abaixo, so apartir do segundo LOOP
        if opcao == '1':
            num1 = float(input("Entre com primeiro numero"))
            # repetir escolha da opradao caso usuario colque errado
            while True:
                escolhaoOeracao = input("Entre com operacoes desejada ('+', '-', '*', '/')")
                operacoes = ['+', '-', '*', '/']
                # if verificar se a entrada das operacoes esta correta
                if escolhaoOeracao in operacoes:
                    break
                else:
                    print("\nOperacao nao valida")
            num2 = float(input("Entre com Segundo numero"))
            # tratar supostos erro na operacao
            try:
                # if para validar as opercoes escolhida
                if escolhaoOeracao == '+':
                    resultado = num1 + num2
                elif escolhaoOeracao == '-':
                    resultado = num1 - num2
                elif escolhaoOeracao == '*':
                    resultado = num1 * num2
                elif escolhaoOeracao == '/':
                    resultado = num1 / num2
                resumo = "Resultado de %.2f %s %.2f = %.2f \n" % (num1, escolhaoOeracao, num2, resultado)
                if resultado % 2 == 0:
                    #open para criar/acrescentar arquivo caso seja par..
                    arquivo = open('calculadora.txt', 'a+')
                    arquivo.writelines(resumo)
                print(resumo)
            except ZeroDivisionError:
                print("Erro para executal operacao\n\n")
        elif opcao == '0':
            print("Voltando Menu Pricipal... \n\n")
            break
        else:
            print("Opcao invalida")
        print("\n+++++++++ MENU CALCULADORA ++++++++")
        opcao = input("| 1 | Calculadora \n| 0 | Menu principal")