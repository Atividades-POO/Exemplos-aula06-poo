# Autores:
# # o exemplo abaixo se encontrar em https://tinyurl.com/2ljnsncx
#
# 4.1 criando a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# 4.4 sobrepondo o método __repr__ para exibição de dados
    def __repr__(self): # representação em formato de string para ser usado em comandos do shell
        return f'Pessoa({self.nome}, {self.idade})'

# 4.5 sobrepondo o método __str__ para exibição de dados
    def __str__(self): # representação em formato de string para ser usado em comandos do shell
        return f'{self.nome} tem {self.idade} anos'

