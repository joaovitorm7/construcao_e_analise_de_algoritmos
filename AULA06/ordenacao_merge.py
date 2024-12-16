def merge_sort(arr):

    if len(arr) <= 1:
        return arr


    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    lista_ordenada = []
    i = j = 0


    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1

    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])
    return lista_ordenada

arr = [38, 27, 43, 3, 9, 92, 10]
print("Lista Original ",arr)
print("Lista Ordenada ",merge_sort(arr))
