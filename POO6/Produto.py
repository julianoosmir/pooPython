class Produto:
    def __init__(self,preco : float,nome:str):
        self.nome = nome
        self.preco = preco
    def __repr__(self):
        return  "%s%s%s%s" % ("nome : ",self.nome," | preco : ",self.preco)

