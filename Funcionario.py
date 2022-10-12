from datetime import date


class Funcionario:
    def __init__(self, codigo: int,nome:str,sobrenome:str,dataNascimento:date):
        self.codigo = codigo
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento

 
funca = Funcionario(1,'mario','carlos',date(2000,2,3))

print(funca.dataNascimento)
