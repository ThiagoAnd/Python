
while True:
    try:
        n, f = [int(x) for x in input("Entre com qtd de amigos e com qtd de frutas: ").split()]
        if 1 <= n <= 103 or 1 <= f <= 103:
            print("Cada amigo tem direito a ", round((f * 0.05) / n, 2), " litros de suco")
        if n == 0 and f == 0:
            break
    except ValueError:
        print("A entrada tem que estar no seguinte formato: N (ESPAÇO) F")
    except ZeroDivisionError:
        print("A quantidade de amigos e de frutas tem que ser maior que 0 e menor que 104")

