import math

resultado = math.sqrt(25)
print(resultado)

from math import sqrt

resultado2 = sqrt(16)
print(resultado2)

import random
import datetime

numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

data_atual = datetime.datetime.now()
print(data_atual)

import meu_modulo

meu_modulo.saudar("Renan")
resultado = meu_modulo.calcular_soma(5, 10)
print(resultado)

import operacoes
import utilidades

resultado_soma = operacoes.somar(3, 7)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado_soma}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")