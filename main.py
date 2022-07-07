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

# 2 - exemplo de uso de uma função


