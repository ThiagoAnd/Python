
def validarZero(numeros):
    cont = 0
    while len(numeros) > cont:

        if numeros[cont] != 0:
            return False
        else:
            True
        cont += 1
    return True

def validarEntrada(numeros):
    cont = 0
    while len(numeros) > cont:

        if numeros[cont] >= 1 and numeros[cont] <= 8:
            print("0")

        else:
            print("1")
            return True
            break
        cont += 1

print("          ###############")
print("          # Introducxao #")
print("          ###############")
print("Os valores devem :mimino 1, maximo 8")
print("A rainha começa na casa de coordenadas (X1,Y1), "
      "\n e a casa de destino é a casa de coordenadas (X2,Y2).")

parada = False
while not parada:
    print("-------------------------------------------------")
    coordenadas = input("Entre com X1 X2 Y1 Y2 ")

    try:
            x1, x2, y1, y2 = map(int, coordenadas.split(' '))
            numeros = [x1, x2, y1, y2]
    except:
        print("Erro na entrada de dados")
        break
    parada = validarZero(numeros)
    if  parada:
        print("-----------------------------")
        print("ENCERRANDO O JOGO")
    elif validarEntrada(numeros):
        print("-----------------------------")
        print("Coordenadas da rainha incorreta")
    inicio = x1 + y1
    partida = x2 + y2
    inicioP = x2 - x1
    partidaP = y2 - y1
    if x1 == x2 or y1 == y2:
        print("\n +_+_+_+_+_+_+")
        print(" 1  movimento ")
        print(" +_+_+_+_+_+_+")
    elif inicio == partida:
        print("\n +_+_+_+_+_+_+")
        print(" 1  movimento")
        print(" +_+_+_+_+_+_+")
    elif inicioP == partidaP:
        print("\n +_+_+_+_+_+_+")
        print(" 1  movimento 3")
        print(" +_+_+_+_+_+_+")
    else:
        print("\n +_+_+_+_+_+_+")
        print(" 2  movimento ")
        print(" +_+_+_+_+_+_+")
