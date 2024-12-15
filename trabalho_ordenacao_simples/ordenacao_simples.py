import random
import time

# BubbleSort Não Otimizado
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# BubbleSort Otimizado
def bubbleSortOtimizado(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# SelectionSort Não Otimizado
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# SelectionSort Otimizado
def selectionSortOtimizado(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# InsertionSort Não Otimizado
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# InsertionSort Otimizado
def pesquisaBinaria(arr, key, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid
    return start

def InsertionSortOtimizado(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = pesquisaBinaria(arr, key, 0, i)
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key

# Função para medir o tempo
def medidaTempo(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

def gerarListaAleatoria(size):
    return [random.randint(0, 10000) for _ in range(size)]

# Testando
listas = [100, 1000, 10000]
algorithms = [
    ("Bubble Sort", bubbleSort),
    ("Bubble Sort Otimizado", bubbleSortOtimizado),
    ("Selection Sort", selectionSort),
    ("Selection Sort Otimizado", selectionSortOtimizado),
    ("Insertion Sort", insertionSort),
    ("Insertion Sort Otimizado", InsertionSortOtimizado),
]

for lista in listas:
    print(f"\nTamanho da lista: {lista}")
    original_list = gerarListaAleatoria(lista)

    for nome, algorithm in algorithms:
        test_list = original_list.copy()
        elapsed_time = medidaTempo(algorithm, test_list)
        print(f"O {nome}: Levou {elapsed_time:.5f} segundos")
