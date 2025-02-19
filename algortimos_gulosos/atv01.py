def merge_sort(lista):
    if len(lista) <= 1: # Confere se a lista já está ordenada
        return lista

    meio = len(lista) // 2 # dividi a lista no meio

    esquerda = merge_sort(lista[:meio]) # ordena a primeira metade
    direita = merge_sort(lista[meio:]) # ordena a segunda metade

    return merge(esquerda, direita) # mescla as duas metades em uma só lista ordenada

def merge(esquerda, direita): # combina as duas listas ordenadas em uma única lista ordenada.
    resultado = [] # lista fazia que vai receber os elementos ordenados
    i = j = 0 # indices para percorrer as duas listas

    while i < len(esquerda) and j < len(direita): # Pecorre a lista e compara os elementos  
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i]) # O menor elemento é adicionado à lista resultado.
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        
    resultado += esquerda[i:] # Se restaram elementos, são adicionados à lista resultado
    resultado += direita[j:]

    return resultado 

def atividade_gulosa(reunioes): # Ordena a lista de reuniões pelo horário de término
    reunioes = merge_sort(reunioes)
    reunioes_selecionadas = [reunioes[0]] # Seleciona a primeira reunião

    for i in range(1, len(reunioes)): # Percorre a lista de reuniões ordenadas 
        if reunioes[i][0] >= reunioes_selecionadas[-1][1]: #Verifica se a próxima reunião começa depois ou exatamente quando a última terminou.
            reunioes_selecionadas.append(reunioes[i]) # Se sim, adiciona a reunião à lista de reuniões selecionadas
    return reunioes_selecionadas

reunioes = [(1, 3), (2, 5), (4, 6), (6, 8), (5, 7)]

reunioes_selecionadas = atividade_gulosa(reunioes)
print("Reuniões Selecionadas: ", reunioes_selecionadas)