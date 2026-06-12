numero = int(input("Digite um numero inteiro:"))
soma_atual = 0
numero_impar = 1
lista_impares = []

for i in range(numero):
    soma_atual += numero_impar
    lista_impares.append(numero_impar)
    if soma_atual >= numero:
        break
    numero_impar += 2
print(lista_impares)