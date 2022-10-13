from datetime import date

class Funcionario:
    def __init__(self, codigo: int,nome:str,sobrenome:str,dataNascimento:date):
        self.codigo = codigo
        self.nome = nome
        self.sobrenome = sobrenome
        self.dataNascimento = dataNascimento
    def __repr__(self):
        return  "%s%s%s%s%s%s%s%s" % ("codigo : ",self.codigo," | nome : ",self.nome, 
            " | sobrenome : ",self.sobrenome," | data de nascimento: ", self.dataNascimento)
 



