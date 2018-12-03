entrada = input()

valores = entrada.split("-")
rg = valores[0]
digito = valores[1]
mult = [2,3,4,5,6,7,8,9]
soma = 0
for i in range (0,len(rg)):
    soma+= mult[i] * int(rg[i])

resto = soma % 11

resto = 11 - resto


if resto == int(digito):
    print("POSITIVO")
else:
    print("NEGATIVO")
