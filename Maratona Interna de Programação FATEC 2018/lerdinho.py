entrada = input()
n = int(input())
nomes = list()
cont=0
saida=""
ult = ""
arroz =""
for i in range(0, n):
    nomes.append(input)


for n in nomes:
    nn = n.split(" ")
    nome = nn[0]
    sobr = nn[1]

    tam = len(entrada)

    if (nome == entrada or sobr == entrada):
        cont += 1
        saida += n+"\n"
    elif (nome.startswith(entrada[0:1]) and sobr.startswith (entrada[1:-1]):
          cont+= 1
          saida += n+"\n"
    elif (nome.startswith(entrada[0:2]) and sobr.startswith (entrada[2:-1]):
