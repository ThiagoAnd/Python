# Dictionary  para armazenar os itens comprados
produtos = {
    1: "Sushi               RS 22.90",
    2: "Sashimi             RS 12.90",
    3: "Salmao              RS 64.90",
    4: "Ramen               RS 5.90",
    5: "Temaki              RS 2.99",
    6: "Yakisoba            RS 10.99",
    7: "Niguiri             RS 13.99"
}


# Funcao relatorio para mostrar as compras feitas
def relatorio():
    print("\n----------Itens comprados------------")
    cont = 0
    matriz = open('compras.txt', 'r')
    for line in matriz:
        cont += 1
        print("%d) %s" % (cont, line))


# Funcao comprar lista os itens do dictionary . Nao sai enquanto nao digitar zero. e a cada compra eu coloco no arquivo compras.txt
def comprar():
    while True:
        print("\n----------Menu de itens------------")
        print("## Digite zero para voltar.##")
        for key, value in produtos.items():
            print("%d ) %s " % (key, value))

        x = int(input("Digite o numero do item a comprar: "))
        if x < 0 or x > len(produtos):
            print("Só pode escolher valores entre 1 e %d \n" % len(produtos))
        elif x == 0:
            return
        else:
            for key, value in produtos.items():
                if x == key:
                    arq = open("compras.txt", "a+")
                    arq.write(value + "\n")
                    arq.close()


# Uso a funcao relatorio para mostrar os itens comprados e utilizo uma logica que copia o conteudo do arquivo compras.txt para uma variavel, apaga o conteudo do arquivo e faz um append com o que esta na variavel
def apagar():
    while True:

        relatorio()
        print("## Digite zero para voltar.##")
        nlinhas = sum(1 for line in open('compras.txt'))

        if nlinhas == 0:
            print("Não existem itens para deletar\n")
        resp = int(input("Digite o numero do item a deletar: "))

        if resp < 0 or resp > nlinhas:
            print("Digite numeros de 1 a %d \n" % nlinhas)
        elif resp == 0:
            return
        # Aqui eh a logica que abre o arquivo, copia para uma variavel todas as linhas , passa por essa variavel e verifica qual item eu quero deletar, utilizo um cont para saber qual linha nao colocar no arquivo compras.txt
        else:
            arquivo1 = open('compras.txt', 'r')
            linhas = arquivo1.readlines();arquivo1.close()
            arquivo1 = open("compras.txt", "w"); arquivo1.close()
            arquivo2 = open("compras.txt", "a+")
            cont2 = 0
            for line in linhas:
                cont2 += 1
                print(line)
                if cont2 != resp:
                    arquivo2.write(line)
            arquivo2.close()

# Funcao principal que faz um while e equanto nao digitar zero nao sai. Por ela faco a chamada das outras funcoes
def index():
    print("+++++++++ MAQUINA DE VENDAS ++++++++++")
    print()

    while True:
        print("|1| Comprar")
        print("|2| Relatorio")
        print("|3| Apagar item")
        print("|0| Menu principal")
        resposta = int(input("Digite uma opçao: "))
        if resposta == 1:
            comprar()
        elif resposta == 2:
            while True:
                relatorio()
                res = int(input("Digite zero para voltar: "))
                if res == 0:
                    break
        elif resposta == 3:
            apagar()
        elif resposta == 0:
            break
        else:
            print("Digite 1,2 ou 3 para as opções\n")

