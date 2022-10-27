from Pessoa import Pessoa

class Individuo(Pessoa):
    def __init__(self, pai:Pessoa,nome:str,idade:int):
        self.pai = pai
        super().__init__(nome,idade)
