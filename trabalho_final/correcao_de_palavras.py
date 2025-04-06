# Importações
import urllib.request
import unicodedata

# Função para normalizar apenas a palavra digitada (removendo acento e caixa alta)
def normalizar(palavra):
    palavra = palavra.lower()
    palavra = ''.join(
        x for x in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(x) != 'Mn'
    )
    return palavra

#Carrega o dicionário do site (mantendo acentos e cedilha)
def carregar_dicionario(url):
    print("Carregando dicionário, aguarde...")
    response = urllib.request.urlopen(url)
    conteudo = response.read().decode("utf-8")
    palavras = conteudo.splitlines()
    print(f"Dicionário carregado com {len(palavras)} palavras.\n")
    return [p.strip() for p in palavras if p.strip()]

# Função de Distância de Levenshtein 
def distancia_levenshtein(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1): dp[i][0] = i
    for j in range(m + 1): dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            custo = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + custo
            )
    return dp[n][m]

#Sugestões de correção ortográfica
def sugerir_correcoes(palavra_digitada, dicionario, X=2, limite=10):
    palavra_normalizada = normalizar(palavra_digitada)
    sugestoes = []

    for termo_original in dicionario:
        termo_normalizado = normalizar(termo_original)
        dist = distancia_levenshtein(palavra_normalizada, termo_normalizado)
        if dist <= X:
            sugestoes.append((termo_original, dist))

    # Ordena por distância e ordem alfabética
    sugestoes.sort(key=lambda x: (x[1], x[0]))

    print(f"\nSugestões para '{palavra_digitada}' (com distância ≤ {X}):")
    if not sugestoes:
        print("Nenhuma sugestão encontrada.")
    else:
        for i, (sugestao, dist) in enumerate(sugestoes[:limite], 1):
            print(f"{i}. {sugestao} (distância: {dist})")
    print("-" * 40)

#Função principal interativa
def modo_interativo():
    URL = "https://www.ime.usp.br/~pf/dicios/br-utf8.txt"
    dicionario = carregar_dicionario(URL)

    print("Sistema de Sugestão Ortográfica (digite 'sair' para encerrar)\n")

    while True:
        entrada = input("Digite uma palavra: ").strip()
        if entrada.lower() == "sair":
            print("Encerrando o sistema. Até mais!")
            break
        elif not entrada:
            print("Digite uma palavra válida!")
            continue
        sugerir_correcoes(entrada, dicionario, X=2, limite=10)

#Início do programa
if __name__ == "__main__":
    modo_interativo()
