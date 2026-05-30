frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

for numero in range(1, 6):
    print(numero * 2)

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

contar = 1

while True:
    print("contar")
    contar += 1
    if contar > 5:
        break


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
