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

matriz(int(input("Digite a ordem da matriz para o quadrado: ")))
