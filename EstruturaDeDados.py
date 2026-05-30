frutas = ["macã", "banana", "laranja"]

print(frutas[0])  # Acessando o primeiro elemento
print(frutas[1])  # Acessando o segundo elemento
print(frutas[2])  # Acessando o terceiro elemento   

print(frutas[-1])  # Acessando o último elemento
print(frutas[-2])  # Acessando o penúltimo elemento
print(frutas[-3])  # Acessando o antepenúltimo elemento

frutas.append("uva")  # Adicionando um elemento ao final da lista
print(frutas)

frutas.insert(1, "abacaxi")  # Inserindo um elemento na posição 1
print(frutas)

frutas.remove("banana")  # Removendo o elemento "banana"
print(frutas)

frutas_removida = frutas.pop(2)  # Removendo o elemento na posição 2 e armazenando-o
print(frutas)
print(frutas_removida)  # Imprimindo o elemento removido

frutas.sort()  # Ordenando a lista em ordem ascendente
print(frutas)

frutas.reverse()  # Invertendo a ordem da lista
print(frutas)

numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]  # Criando uma nova lista com os quadrados dos números pares
print(quadrados)
