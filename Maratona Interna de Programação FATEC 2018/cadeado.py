
entrada = input()
saida = ""
valores = entrada.split(" ")
atual = valores[1]
senha = valores[2]
    
controle = 0
direcao =""
for i in range(0,int(valores[0])):
    controle = int(atual[i]) - int(senha[i])
    if controle < 0:
        controle = controle * -1
        if int(atual[i]) >= int(senha[i]):
            direcao = ""
        if int(atual[i]) < int(senha[i]):
            direcao = "-"
        if controle > 5:
            controle = 10 - controle
            direcao = "-"
            
        if controle == 0:
            saida += "0"
        for j in range(0, controle):
            saida+=direcao+"1"

            saida +=" "

print (saida)    

outrasaida = ""
for i in range(0, len(saida)-1):
    outrasaida += saida[i]
print(outrasaida)



                                   


              
