from Pessoa import Pessoa
from Livro import Livro
class Emprestimo:
    def __init__(self,emprestador: Pessoa,emprestante : Pessoa,livro : Livro):
        self.emprestador = emprestador
        self.emprestador = emprestante