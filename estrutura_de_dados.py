#lista
lista = ['Amanda Amorim', 9.5, 10, 8.5, True]
print(lista)
print(lista[-1])

#forma dinâmica de leiura da estrutura
for elemento in lista:
    print(elemento)
    
#atualização de elementos
lista[3] = 10.0
print(lista)

#calculo de média
media = (lista[1] + lista[2] + lista[3])/3
print(media)