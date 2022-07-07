#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 06/07/2022
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

print("_________________________________________________")
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

print("_________________________________________________")

########################################################################################################################

# 3 - Passando vários argumentos para um
# método de instanciação de uma classe.
# Quando precisamos passar uma indeterminada quantidades de paramentos para uma classe, método ou função, temos
# basicamente a opções de uma coleção de forma posicional ou por chaves.
# Para isso usamos o operador de descompactação ( *) para argumentos posicional e (**) para uso com chaves.
# posicional: *args # argumentos (um interavel, lista, tupla, etc.)
# chaves: **kwargs # argumentos comm chaves (um dicionário)
#
# exemplo de uso de passagem de varios argumentos em uma função:
def func_args(*args):
    print(f'tipo: {type(args)} conteúdo: {args}') # exibição do tipo e conteúdo da tupla *args
    for arg in args:  # percorre os argumentos da tupla *args
        print(f'tipo: {type(arg)} conteúdo: {arg}') # exibição do tipo e conteúdo dos argumentos da tupla *args

# chamando a função func_args com varios argumentos
func_args(1, 'A', {'valor': 10}) # passagem de 3 paramentos para a função func_args
# a saída da função func_args é:
# um INT, um STRING e um DICIONÁRIO

# 3.1 exemplo, criação de uma classe que recebe vários argumentos
# class Equacao:
from equacao import Equacao as E # importação da classe Equacao da biblioteca equacao.py
e1 = E(1, 0, -4, 3, 0, 4, 5) # instanciação de objeto da classe Equacao
print(e1.indices) # exibição dos indices da equação e1 em forma de lista
# voltaremos a classe Equacao mais a frente

print("_________________________________________________")

########################################################################################################################
# o exemplo abaixo se encontrar em https://tinyurl.com/2ljnsncx
# 4 - introdução ao método especial __repr__
# método especial __repr__ é usado para representação de dados
# exemplo de uso de __repr__, crie a classe pessoa e implemente o método __repr__
# 4.1 importação da classe pessoa
from pessoa import Pessoa as P
# 4.2 instanciação da classe pessoa
p1 = P('Davi', 10) # instanciação de objeto da classe Pessoa com nome 'Davi' e idade 10
# 4.3 exibição do objeto p1
''' print(p1) # exibição do objeto p1 '''
# por padrão a exibição do objeto p1 é: <pessoa.Pessoa object at 0x000002543C4021A0>  o endereço do objeto pode mudar

# comente o print acima
# 4.4 exibição do objeto p1 em forma de string podemos sobrepor o método __repr__ (na classe pessoa)
''' print(p1) # exibição do objeto p1 agora é Pessoa(Davi, 10)'''

# Quando uma classe não implementa o __str__método e você passa uma instância dessa classe para o str(), Python
# retorna o resultado do método __repr__  porque internamente o método __str__ chama o método __repr__

# comente o print acima
# 4.5 exemplo de uso de __str__
# Se uma classe implementar o __str__método, o Python chamará o __str__método quando você passar uma
# instância da classe para o str(). Por exemplo, vamos sobrepor o método __str__ para a classe Pessoa:
print(p1) # exibição do objeto p1 agora é 'Davi tem 10 anos'

# 4.6 da mesma forma que podemos passar um objeto ou valor para o str(), podemos passar um objeto ou valor para o repr()
print(repr(p1)) # exibição do objeto p1 agora é Pessoa(Davi, 10)
print(str(p1)) # exibição do objeto p1 agora é 'Davi tem 10 anos'
print(p1.__str__()) # chamada de método __str__ para exibição de dados em formato de string
print(p1.__repr__()) # chamada de método __repr__ para exibição de dados em formato de string

