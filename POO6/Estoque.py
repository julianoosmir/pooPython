from Produto import Produto

class Estoque:
    def __init__(self,iten: Produto,quantidade: int):
        self.iten = iten
        self.quantidade = quantidade
    def __repr__(self):
        return  "%s%s%s%s%s%s%s%s" % ("\n","nome : ",self.iten.nome, " | valor unitario : ",self.iten.preco,
                                  " | quantidade: ", self.quantidade,"\n")