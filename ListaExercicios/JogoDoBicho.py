import random

print("++++++ JOGO DO BICHO ++++++++")
while True:
    try:
        numeroSorteado = str(random.randint(0, 1000000))
        print("Entre com os seguinte valores")
        valorAposta, numeroAposta = input("Valor da Aposta e numero escolhido para aposta").split(' ')
        valorAposta = float(valorAposta)
        print("Valor aposta -> %.2f numero da aposta -> %s  valor sorteado -> %s" % (valorAposta, numeroAposta, numeroSorteado))
        i = int(len(numeroSorteado) - 1)
        j = int(len(numeroAposta) - 1)
        numererosIguais = 0
        while True:
            if numeroSorteado[i] == numeroAposta[j]:
                numererosIguais +=1
            else:
                break
            i -=1
            j -=1
            if i < 0 or j < 0:
                break
        if valorAposta > 1000.00 or int(numeroAposta) > 1000000:
            print("Valor da aposta nao pode passar de 1000.00 e o numero nao pode passsa de 1000000")
        elif numererosIguais == 4:
            print("Ganhou -> %.2f "% (valorAposta * 3000))
        elif numererosIguais == 3:
            print("Ganhou -> %.2f "% (valorAposta * 500))
        elif numererosIguais == 2:
            print("Ganhou -> %.2f "% (valorAposta * 50))
        else:
            numSor = numeroSorteado[i-1] + numeroSorteado[i]
            numEs = numeroAposta[j-1] + numeroAposta[j]
            intervalo = []
            cont = 0
            grupo = False
            for i in range(1, 101):
                cont += 1
                if i == 100:
                    intervalo.append(00)
                intervalo.append(i)
                if cont == 4:
                    if numSor in intervalo and numEs in intervalo:
                        grupo = True
                        break
                    else:
                        intervalo = []
                        cont = 0
            if grupo:
                print("Ganhou -> %.2f " % (valorAposta * 16))
            else:
                print("Nao ganhou nada")

    except:
        print("Erro na entrada de dados")