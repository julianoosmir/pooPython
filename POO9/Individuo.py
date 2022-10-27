from Pessoa import Pessoa

class Individuo(Pessoa):
    def __init__(self,nome:str,idade:int, pai:Pessoa,mae:Pessoa):
        self.pai = pai
        self.mae = mae
        super().__init__(nome,idade)
    def __repr__(self):
        return super().__repr__() + "%s%s%s%s" % ("| pai : ",self.pai.nome ,"| mae: ", self.mae.idade)
