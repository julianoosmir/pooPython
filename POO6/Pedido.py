from Produto import Produto

class Pedido:
    def __init__(self,iten: Produto,quantidade: int):
        self.iten = iten
        self.quantidade = quantidade
    def __repr__(self):
        return  "%s%s%s%s" % ("nome : ",self.iten.nome," | quantidade: ", self.quantidade)
