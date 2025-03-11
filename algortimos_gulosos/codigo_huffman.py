class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def huffman_coding(text):
    # Contar a frequência de cada caractere
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    # Criar uma lista de nós oiutra forma de fazer: nodes = [Node(char, freq) for char, freq in freq_dict.items()]
    nodes = []  # Cria uma lista vazia
    for char, freq in freq_dict.items():  # Itera sobre os pares do dicionário
        new_node = Node(char, freq)  # Cria um novo nó
        nodes.append(new_node)  # Adiciona o nó à lista
    
    # Construir a árvore de Huffman
    while len(nodes) > 1:
        # Ordenar por frequência
        nodes.sort(key=lambda x: x.freq)
        
        # Pegar os dois nós com menores frequências
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        # Criar nó pai
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        
        # Adicionar pai de volta à lista
        nodes.append(parent)
    
    return nodes[0] if nodes else None

def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    # Se for uma folha (tem caractere)
    if root.char is not None:
        codes[root.char] = current_code if current_code else "0"
        return codes
    
    # Percorrer à esquerda (0)
    if root.left:
        generate_codes(root.left, current_code + "0", codes)
    
    # Percorrer à direita (1)
    if root.right:
        generate_codes(root.right, current_code + "1", codes)
    
    return codes

# Teste do código
text = "abracadabra"

# Construir a árvore de Huffman
root = huffman_coding(text)

# Gerar os códigos
codes = generate_codes(root)

# Mostrar os códigos para cada caractere
print("Códigos de Huffman:")
for char, code in codes.items():
    print(f"'{char}': {code}")

# Calcular total de bits
total_bits = 0
for char in text:
    total_bits += len(codes[char])

print(f"\nTexto original: {text}")
print(f"Tamanho original (8 bits por char): {len(text) * 8} bits")
print(f"Tamanho comprimido: {total_bits} bits")
print(f"Taxa de compressão: {(1 - total_bits/(len(text)*8))*100:.2f}%")