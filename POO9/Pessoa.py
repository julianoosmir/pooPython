class Pessoa(object):
    def __init__(self, nome: str,idade:int):
        self.idade = idade
        self.nome = nome
    def __repr__(self):
        return  "%s%s%s%s" % ("nome : ",self.nome ," | idade : ",self.idade)