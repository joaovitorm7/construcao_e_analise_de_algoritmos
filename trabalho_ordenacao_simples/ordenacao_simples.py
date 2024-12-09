# Bubble Sort - Versão não otimizada
def bubbleSort(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

# Bubble Sort - Versão Otimizada
def bubbleSortOrimizado(lista):
    n = len(lista)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                swapped = True
            if not swapped:
                break

# Selection Sort - Versão não otimizada
def selectionSort(lista):
    n = len(lista)

    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if lista[j] < lista[minIndex]:
                minIndex = j
            temp = lista[i]
            lista[i] = lista[minIndex]
            lista[minIndex] = temp

# Selection Sort - Versão otimizada
def selectionSortOtimizado(lista):
    n = len(lista)

    for i in range(n):
        minIndex = i
        for j in range(n + 1, n):
            if lista[j] < lista[minIndex]:
                minIndex = j
            if minIndex != i:
                temp = lista[i]
                lista[i] = lista[minIndex]
                lista[minIndex] = temp

# Insertion Sort - Versão não otimizada
def insertionSort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while(j >= 0 and lista[j] > chave):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

# Insertion Sort - Versão otimizada Binary
def BinaryInsertionSort(lista):
    