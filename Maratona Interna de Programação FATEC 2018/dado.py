quantjogadas = int(input())
dados=input()
dados = dados.split(" ")
somaLuiza=0
somaAntonio=0
controle=0
for n in dados:
    if (controle==0):
        somaLuiza= somaLuiza+ int(n)
        print("l ",n)
        if (int(n) != 6):
            controle=1
    else:
        somaAntonio= somaAntonio + int(n)
        print("a ",n)
        if (int(n) != 6):
            controle=0

            
if (somaLuiza>somaAntonio):
    print("LUIZA",somaLuiza)
elif(somaLuiza<somaAntonio):
     print("ANTONIO",somaAntonio)
else:
    print("EMPATE",somaAntonio)
        
        
