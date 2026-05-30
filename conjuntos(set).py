
# Conjuntos (Set) em Python
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2 # União dos conjuntos
print("Uniao:", uniao)

intersecao = conjunto1 & conjunto2 # Interseção dos conjuntos
print("Intersecao:", intersecao)

diferenca = conjunto1 - conjunto2 # Diferença dos conjuntos
print("Diferenca:", diferenca)

diferenca_simetrica = conjunto1 ^ conjunto2 # Diferença simétrica dos conjuntos
print("Diferenca Simetrica:", diferenca_simetrica)

frutas.add("pera")
print("Frutas:", frutas)

frutas.remove("banana")
print(f"Frutas após remoção: {frutas}")

frutas.discard("uva") # Não gera erro se o elemento não existir
print(f"Frutas após tentativa de remoção de 'uva': {frutas}")

frutas.clear() # Limpa o conjunto
print(f"Frutas após limpeza: {frutas}")