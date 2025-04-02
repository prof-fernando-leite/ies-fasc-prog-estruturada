def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

s1 = input("Digite a primeira palavra: ")
s2 = input("Digite a segunda palavra: ")
print(sao_anagramas(s1, s2))
