#
# Autores:
# Michel Silva
# Emanuel Frank
# Carlos Eduardo
# data: 06/07/2022
#
######     3.1 - Passando vários argumentos para um método de instanciação de uma classe
# #
class Equacao:

  def __init__(self, *indices):  # inicialização de um objeto da classe Equacao
    # self.indices = indices # print(e1.indices) sai como uma tupla de indices
    self.indices = list(indices)  # print(e1.indices) sai como uma lista de indices
    # print(f'Equacao criada com os indices: {self.indices}') # exibição dos indices da equação

# ########################################################################################################################
# 5 - implementação dos métodos __repr__ e __str__
# #
# # método __repr__: representação de um objeto
# # método __str__: exibição de um objeto
# #
# # exemplo de uso de __repr__ e __str__
# #
  def __repr__(self):
    # retorar a representação string da classe Equacao
    # só para dedmostração, vamos fazer um cast para tupla
    return f'Equacao = {tuple(self.indices)}'

  def __str__(self):
    # vamos implentar o método __str__ para exibição de um objeto da classe Equacao
    # no formato de uma equação matemática, se entramos os valores (2, 0, 3, 5) vamos exibir:
    # o retorno será: 2x^3 + 3x + 5
