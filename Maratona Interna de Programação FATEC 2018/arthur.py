entrada = int(input())
palavras = list()
for i in range(0,entrada):
    palavras.append(input())
frase = input()

for n in palavras:
    giria = n.split(" ")
    frase = frase.replace(giria[0],giria[1])

print(frase)
    
