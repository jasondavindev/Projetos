# Problema numero 1008

tabela = {
    "A": [3, 10],
    "C": [5, 15],
    "S": [1, 5]
}

sexos = ["H", "M"]
qtdConsultas = 0
saida = []

while True:
    qtdConsultas += 1
    entrada = input()

    if (entrada == "0"):
        break

    entrada2 = entrada.split(" ")
    consultas = int(input())
    vetPessoas = []
    qtdBanheiros = int(entrada2[0])
    evento = entrada2[1]
    banheiros = []

    for i in range(qtdBanheiros):
        banheiros.append({"numero": (i + 1), "tempo": 0})

    idPessoas = list(map(lambda x: int(x), input().split(" ")))

    cloneIdPessoas = idPessoas.copy()
    idPessoas.sort()
    maiorId = idPessoas[-1]

    for i in range(maiorId):
        if evento == "A":
            if (i % 3 == 0):
                idx = 0
            else:
                idx = 1
        elif evento == "C":
            if (i % 4 == 0):
                idx = 0
            else:
                idx = 1
        elif evento == "S":
            if ((i + 1) % 3 == 0):
                idx = 1
            else:
                idx = 0

        banheiros = sorted(banheiros, key=lambda k: k['numero'])
        banheiroOrdenado = sorted(banheiros, key=lambda k: k['tempo'])
        banheiroEscolhido = banheiroOrdenado[0]
        vetPessoas.append(
            {"sexo": sexos[idx], "banheiro": banheiroEscolhido["numero"], "tempo": banheiroEscolhido["tempo"]})
        banheiroEscolhido["tempo"] += tabela[evento][idx]
        banheiros = banheiroOrdenado

    saida.append(("Consulta " + str(qtdConsultas) + ":"))
    for i in cloneIdPessoas:
        minhaPessoa = vetPessoas[i - 1]
        saida.append((str(minhaPessoa["tempo"]) + " " + str(minhaPessoa["banheiro"]) + " " + minhaPessoa["sexo"]))

print('\n'.join(saida))