def selectionSort(lista):
    n = len(lista)

    for i in range(n - 1):
        minIndex = i   
        for j in range(i + 1, n):
            #print("J=",lista[j])
            #print("MinIndex=",lista[minIndex])
            if lista[j] < lista[minIndex]:
                minIndex = j
        if minIndex != i:
            temp = lista[i]
            lista[i] = lista[minIndex]
            lista[minIndex] = temp

    return lista

numeros = [8, 5, 2, 3]

print("Lista Normal: ",numeros)
ordenadas = selectionSort(numeros)
print("Lista Ordenada 1: ",ordenadas)

def selectionSortMenorMaior(lista):
    if not lista:
        return None, None, lista 

    menor = maior = lista[0] 
    n = len(lista)  

    for i in range(n - 1):  
        minIndex = i  

        for j in range(i + 1, n):
            if lista[j] < lista[minIndex]:  
                minIndex = j  

            if lista[j] < menor:
                menor = lista[j]
            elif lista[j] > maior:
                maior = lista[j]

        if minIndex != i:
            temp = lista[i]  
            lista[i] = lista[minIndex] 
            lista[minIndex] = temp 

    return menor, maior, lista

numeros = [38, 15, 27, 49, 10, 12, 22, 33]

menor, maior, ordenados = selectionSortMenorMaior(numeros)
print("Lista Normal:", numeros)
print("Lista ordenada 2:", ordenados)
print("Menor elemento:", menor)
print("Maior elemento:", maior)

