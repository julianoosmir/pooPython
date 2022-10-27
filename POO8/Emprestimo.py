from Pessoa import Pessoa
from Livro import Livro
class Emprestimo:
    def __init__(self,emprestador: Pessoa,emprestante : Pessoa,livro : Livro):
        self.emprestador = emprestador
        self.emprestante = emprestante
        self.livro = livro
    def __repr__(self):
        return "%s%s%s%s%s" % (self.emprestador.nome," emprestou o livro ", self.livro.nome," para ",self.emprestante.nome)
