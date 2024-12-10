def MergeSort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    left = MergeSort(lista[0:meio])
    right = MergeSort(lista[meio: ])

    return Merge(left, right)

def Merge(left, right):
    listaOrdenada = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            listaOrdenada.append(left.pop(0))
        else:
            listaOrdenada.append(right.pop(0))

    listaOrdenada.extend(left) 
    listaOrdenada.extend(right) 
    return listaOrdenada

listaTeste = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", listaTeste)
resultado = MergeSort(listaTeste)
print("Lista ordenada:", resultado)




