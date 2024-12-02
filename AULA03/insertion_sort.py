def InsertionSort(lista):
    n = len(lista)

    for i in range(n):
        chave = lista[i]
        j = i - 1

        while(j >= 0 and lista[j] > chave):
            lista[j + 1] = lista[j]
            j = j - 1
        
        lista[j + 1] = chave
    return lista

numeros = [10, 2, 8, 5]
print("Números desordenados: ",numeros)
ordenados = InsertionSort(numeros)
print("Números ordenados: ",ordenados)
