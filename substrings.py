# Dada uma string, encontre o comprimento da substring mais longa sem caracteres repetidos.
def substring_sem_repetir(s):
    char_index = {}
    inicio = max_tamanho = 0
    for fim, char in enumerate(s):
        if char in char_index and char_index[char] >= inicio:
            inicio = char_index[char] + 1
        char_index[char] = fim
        max_tamanho = max(max_tamanho, fim - inicio + 1)
    return max_tamanho

s1 = input("Digite a uma palavra: ")
print(f"Tamanho da maior substring sem repetir: {substring_sem_repetir(s1)}")