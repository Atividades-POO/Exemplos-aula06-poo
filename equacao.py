#
######     3.1 - Passando vários argumentos para um método de instanciação de uma classe
# #
class Equacao:

  def __init__(self, *indices):  # inicialização de um objeto da classe Equacao
    # self.indices = indices # print(e1.indices) sai como uma tupla de indices
    self.indices = list(indices)  # print(e1.indices) sai como uma lista de indices
    # print(f'Equacao criada com os indices: {self.indices}') # exibição dos indices da equação
