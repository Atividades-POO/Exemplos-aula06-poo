#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 26/06/2022
#
# encapsulamento de dados
# métodos REPR e STR para representação e exibição de dados
#
# 1 - exemplo calculo de uma função
# antes de tudo, vamos criar um exempo de uso de uma função para calcular o valor de um
# polinômio de grau 4:
# x^4 - 4x^2 + 3x
#
def p(x): # função para calcular o valor de um polinômio de grau 4
    return x**4 - 4*x**2 + 3*x # expressão do polinômio de grau 4

for x in [-1, 0, 2, 3.4]: # teste de valores para x para o polinômio de grau 4
    print(f'passando p({x}) = {p(x)}') # exibição do valor de p(x) para x = -1, 0, 2, 3.4 respectivamente

########################################################################################################################

# 2 - exemplo de uso de passagem de varios argumentos
l1 = [1,2,3,4,5] # criação de uma lista com 5 elementos
print(l1) # exibição da lista l1 com 5 elementos [1, 2, 3, 4, 5]
print(type(l1)) # exibição do tipo da lista l1 <class 'list'>
# veja que não precisamos importar a classe lista
# ex. from algo import Algo as A
# a1 = A() # instanciação de objeto A
# também não precisamos definir quantos argumentos que podemos passar para a instanciação da classe lista
# agora para nossa classe Algo, o inicializador deve receber um argumento compactado, veremos mais a frente

# exemplo de uso de passagem de varios argumentos como uma tupla
t2 = (1,2,3,4,5) # criação de uma tupla com 5 elementos
print(t2) # exibição da tupla t2 com 5 elementos (1, 2, 3, 4, 5)
print(type(t2)) # exibição do tipo da tupla t2 <class 'tuple'>
l2 = list(t2) # criação de uma lista a partir da tupla t2
print(l2) # exibição da lista l2 com 5 elementos [1, 2, 3, 4, 5]
print(type(l2)) # exibição do tipo da lista l2 <class 'list'>

########################################################################################################################

# 3 -