num = int(input("Numeros: "))
lista = []
while num>0:
    lista.append(num)
    num = int(input("Numeros: "))

print ("Numero maximo: %d" %max(lista))

for elemento in lista:
    if elemento % 2 ==0:
        print ("Numero par: " +str(elemento))
