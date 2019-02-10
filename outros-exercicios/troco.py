# Problema numero 1010

numCasos = int(input())
casos = []

for i in range(numCasos):
    qtdProds = int(input())
    valor = 0

    for p in range(qtdProds):
        produto = list(map(lambda n: int(n), input().split(" ")))
        valor += produto[0] * produto[1]

    pago = int(input())
    troco = pago - valor

    if (troco < 0):
        casos.append('DINHEIRO INSUFICIENTE')
    else:
        casos.append(str(troco))

print('\n'.join(casos))