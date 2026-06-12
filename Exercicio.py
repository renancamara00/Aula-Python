rodadas = int(input("Digite o numero de rodadas:"))
soma = 0
contJ = 0
contM = 0

for i in range(rodadas):
    Joao = int(input("Digite um numero de 0 a 5:"))
    Maria = int(input("Digite um numero de 0 a 5:"))
    soma = Joao + Maria
    if soma % 2 == 0:
        print("Joao ganhou")
        contJ += 1
    else:
        print("Maria ganhou")
        contM += 1

print(f"Joao ganhou {contJ} vezes")
print(f"Maria ganhou {contM} vezes")

quantidadeProdutos = int(input("Digite a quantidade de produtos:"))
precoTotal = 0

for i in range(quantidadeProdutos):
    preco = float(input("Digite o preço do produto:"))
    precoTotal += preco

print(f"O preço total é: {precoTotal}")