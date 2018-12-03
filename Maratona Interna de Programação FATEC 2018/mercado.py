entrada = int(input())
otae = input()
numero = otae.split(" ")
menor = 0
for i in range(0, len(numero)):
    for n in range(i+1,len(numero)):
        if int(numero[i]) - int(numero[n]) > menor:
            menor = int(numero[i]) - int(numero[n])


menor = menor * -1
print(menor)
    
    
