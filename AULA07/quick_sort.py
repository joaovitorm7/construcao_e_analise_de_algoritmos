def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivo = arr[-1]

    elementosMenores = []
    elementosMaiores = []

    for x in arr[:-1]:
        if x <= pivo:
            elementosMenores.append(x)
        else:
            elementosMaiores.append(x)
    
    return quickSort(elementosMenores) + [pivo] + quickSort(elementosMaiores)

arr = [10, 8, 3, 2, 5]
print("Lista Original: ", arr)
listaOrdenada = quickSort(arr)
print("Lista Ordenada: ", listaOrdenada)
