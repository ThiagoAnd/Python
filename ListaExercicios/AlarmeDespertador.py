while True:
    try:
        H1, M1, H2, M2 = map(int, input("Digite a hora corrente e a hora do alarme no seguinte formato \n Hc Mc Ha Ma : ").split(' '))
        if ((0 > H1) or (0 > M1) or (0 > H2) or (0 > M2)) or ((H1 > 23) or (H2 > 23) or (M1 > 59) or (M2 > 59)):
            raise AttributeError
        if 0 == H1 == H2 == M1 == M2:
            print("Volte sempre!")
            break
        HoraFim = (H2 * 60) + M2
        if H2 > H1:
            HoraInicio = (H1 * 60)+M1
            print("O intervalo de tempo para descanço sera de %d minutos" % (HoraFim - HoraInicio))
        else:
            HoraInicio = 1440 - ((H1 * 60)+M1)
            print("O intervalo de tempo para descanço sera de %d minutos" % (HoraFim + HoraInicio))
    except ValueError:
        print("\nA entrada tem que estar no seguinte formato: Hc (ESPACO) Mc (ESPACO) Ha (ESPACO) Ma")
    except AttributeError:
        print("\nAs Horas devem estar no range de 0 a 23 e os minutos de 0 a 59")
