def matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            if (0 < i < n-1) and (0 < j < n-1):
                linha.append(" ")
            else:
                linha.append("x")
        matriz.append(linha)
        print(matriz[i])

    arq = open("c:\\Users\\s4lez\\Desktop\\THIAGO\\Python\\ListaExercicios\\LogMatrizQuadrada.txt", "a+")
    arq.write("\nDigite a ordem da matriz para o quadrado: \n")
    arq.write("Resposta = %d \n\n" % n)
    for i in range(n):
        arq.write(str(matriz[i]) + "\n")

    arq.close()
    print("\n Foi gerado um log no arquivo LogMatrizQuadrada.txt")
matriz(int(input("Digite a ordem da matriz para o quadrado: ")))