from Livro import Livro
from Pessoa import Pessoa
from Emprestimo import Emprestimo

livro = Livro('DDD','eric','tech')
emprestador = Pessoa('mateus','mesmo')
emprestante = Pessoa('jorge','pessoa')

print(Emprestimo(emprestador,emprestante,livro))





