def saudacao (nome):
    return print(f"Olá, {nome}! Bem-vindo(a) ao Python!")

saudacao("Renan")

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(resultado)

# funções anonimas (lambda)

quadrado = lambda x: x ** 2
print(quadrado(5))

# escopo de variáveis (local e global)

def funcao(): 
    variavel_local = 10
    print(variavel_local) # Variável local, só existe dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global) # Variável global, pode ser acessada em qualquer lugar do código

funcao()
funcao2()
print(variavel_global)
# print(variavel_local) Isso vai gerar um erro, pois variavel_local não é acessível fora da função funcao()

#docstrings

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.
    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.
    Returns:
        float: A área do retângulo.
    """
    return base * altura

#funções com numero variavel de argumentos

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(soma_variavel(1, 2, 3, 4, 5))
print(soma_variavel(10, 20))
