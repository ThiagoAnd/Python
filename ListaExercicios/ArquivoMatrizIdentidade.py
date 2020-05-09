import os
import time
def matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
        print(matriz[i])

    arq = open("c:\\Users\\s4lez\\Desktop\\THIAGO\\Python\\ListaExercicios\\LogMatrizIdentidade.txt", "a+")
    arq.write("\nDigite a ordem da matriz: \n")
    arq.write("Resposta = %d\n\n"%n)
    for i in range(n):
        arq.write(str(matriz[i])+"\n")

    arq.close()
    print("\n Foi gerado um log no arquivo LogMatrizIdentidade.txt")
    try:
        os.startfile('c:\\Users\\s4lez\\Desktop\\THIAGO\\Python\\ListaExercicios\\LogMatrizIdentidade.txt')
        time.sleep(5.5)
        os.system('TASKKILL /F /IM notepad.exe')
    except:
        print("Um erro aconteceu ao tentar abrir o arquivo")


matriz(int(input("Digite a ordem da matriz: ")))