numeroTimes = ''
numeroJogadas = ''
def validacaonumTimes(numeroTimes):
    if numeroTimes < 2:
        return False
    if numeroTimes > 200:
        print("--------200    :",numeroTimes)
        return False
    else:
        return True

def validacaonumJogadas(numeroJogadas):
    if numeroJogadas < 0:
        return False
    if numeroJogadas > 104:
        return False
    else:
        return True

parada = False
while not parada:
    print('\n*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
    print('-------------------LIGA FAPI--------------------------------')
    print('\n*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
    entrada = input("informe: Numero de times  e numero de jogadas ")
    if entrada == '0':
        print('\n*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/')
        print('-------------------ATE MAIS--------------------------------')
        parada = True
        break
    try:
        numeroTimes, numeroJogadas = map(int, entrada.split(' '))

    except:
        print("Erro na entrada de dados")
        break


    if not validacaonumTimes(numeroTimes):
        print("\n=====================================================")
        print("numero de times nao valido: minimo 2 e maximo 200 -> %s",numeroTimes)
        print("=====================================================")
    elif not validacaonumJogadas(numeroJogadas):
        print("\n=====================================================")
        print("numero de jogadas nao valida: minimo  e maximo 104")
        print("=====================================================")
    else:
        empates = 0
        for i in range(1, numeroJogadas + 1):
            entrada2 = input("informe: nome  do %iº times  e pontuação sua atual " % i)

            try:
                nomeTime, pontuacao = map(str, entrada2.split(' '))
                pontuacao = int(pontuacao)
                print(pontuacao,nomeTime)
                while len(nomeTime) > 10:
                    print("\n===============!!!!!!!!!!!!!=================")
                    nomeTime = input(" ERRO informe: nome do TIME novamente deve conter no maximo 10 palavras ")
                    print("====================================================")

                empates += pontuacao % 3

            except:
                print("Erro na entrada de dados")
                break
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print("Numero de empate: %d", empates)
            print("