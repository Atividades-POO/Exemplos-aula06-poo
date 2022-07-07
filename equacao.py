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
    #
    grau = len(self.indices) - 1 # grau da equação (número de termos) - 1 (para o grau ser o número de termos menos 1)
    # print(f'grau = {grau}')
    simbolo = '' # inicialização do simbolo da equação podendo ser qualquer caractere, vamos iniciar com vazio
    def expoente(grau):
      if grau == 0:
        simbolo = ''
      elif grau == 1:
        simbolo = 'x'
      else:
        simbolo = 'x^' + str(grau)
      return simbolo

    for i in range(0, grau + 1):
      indice = self.indices[i]
      # nada precisa ser feito se o indice for 0
      if abs(indice) == 1 and i < grau:
        # 1 na frente do x não deve ocorrer nada, por exemplo, x em vez de 1x
        # mas precisamos do sinal do mais ou do menos:
        # simbolo += f"{'+' if indice > 0 else '-'}{expoente(grau - i)}"
        simbolo = simbolo + f"{'+' if indice > 0 else '-'}{expoente(grau - i)}"
      elif indice != 0: # se o indice for diferente de 0 então devemos adicionar o sinal do mais ou do menos e o indice
        simbolo = simbolo + f"{indice:+g}{expoente(grau - i)}" # g para formatar o número como float com duas casas decimais e sem sinal
    return simbolo.lstrip('+') # remove o sinal de mais do início da string se existir (se não existir não faz nada)


