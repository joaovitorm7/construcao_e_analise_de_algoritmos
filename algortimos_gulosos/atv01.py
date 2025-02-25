def merge_sort(lista):
    if len(lista) <= 1: 
        return lista

    meio = len(lista) // 2 

    esquerda = merge_sort(lista[:meio]) 
    direita = merge_sort(lista[meio:]) 

    return merge(esquerda, direita) 

def merge(esquerda, direita): 
    resultado = [] 
    i = j = 0 

    while i < len(esquerda) and j < len(direita):  
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i]) 
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        
    resultado += esquerda[i:] 
    resultado += direita[j:]

    return resultado 

def atividade_gulosa(reunioes): 
    reunioes = merge_sort(reunioes)
    reunioes_selecionadas = [reunioes[0]] 

    for i in range(1, len(reunioes)): 
        if reunioes[i][0] >= reunioes_selecionadas[-1][1]: 
            reunioes_selecionadas.append(reunioes[i]) 
    return reunioes_selecionadas

reunioes = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]

reunioes_selecionadas = atividade_gulosa(reunioes)
print("Reuniões Selecionadas: ", reunioes_selecionadas)