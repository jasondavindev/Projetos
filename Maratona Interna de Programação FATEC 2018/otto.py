entrada= int(input())
nome=list()
for i in range(0,entrada):
    nome.append(input())

for n in nome:
    if(n == n[::-1]):
        print("sim")
    else:
        print("nao")
