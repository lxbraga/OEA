import struct

qtd = input("\n\nDigite a quantidade de registros por bloco\n\n")
colunaCEP = 5
registroCEP = struct.Struct("72s72s72s72s2s8s2s")

f = open("cep.dat", "rb")
f2 = open("cep2.dat", "w")

lista = list()
count = 0

def compara(a, b):
    if a[colunaCEP] == b[colunaCEP]: return 0
    if a[colunaCEP] > b[colunaCEP]: return 1
    return -1

linha = f.read(registroCEP.size)

while linha != "":

    while linha != "" and count < qtd:
        count = count+1
        tmp = registroCEP.unpack(linha)
        lista.append(tmp)
        linha = f.read(registroCEP.size)

    lista.sort(compara)

    for l in lista:
        f2.write(registroCEP.pack(*l))

    lista = []
    count = 0

f.close()
f2.close()

print ("FIM")
