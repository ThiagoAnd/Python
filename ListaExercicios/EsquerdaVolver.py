while True:
    try:
        N = int(input("\nDigite o numero de movimentos(1 a 1000) : "))
        if N == 0:
            print("Obrigado por jogar")
            break
        if N not in range(1, 1001):
            raise AttributeError

        while True:
            resp = input("Digite a lista de comandos: ").upper()
            if resp.count("E") + resp.count("D") == N:
                break
            else:
                print("Digite %d letra(s) contendo apenas 'E' e/ou 'D'" % N)

        e = resp.count("E")
        d = resp.count("D")
        cont = 4

        if e > d:
            move = e - d
            for i in range(move):
                cont -= 1
                if cont == 0:
                    cont = 4

        elif d > e:
            move = d - e
            for i in range(move):
                cont += 1
                if cont == 5:
                    cont = 1

        if cont == 4:
            print("Terminou no NORTE")
        if cont == 3:
            print("Terminou no OESTE")
        if cont == 2:
            print("Terminou no SUL")
        if cont == 1:
            print("Terminou no LESTE")

    except AttributeError:
        print("\nDigite numeros de 1 a 1000")
    except ValueError:
        print("\nDigite apenas numeros ")
