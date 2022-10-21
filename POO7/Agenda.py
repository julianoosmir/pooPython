from Contato import Contato
class Agenda:
    def __init__(self,contatos:list):
        self.contatos = contatos
    def mostrarAgenda(self):
        print(self.contatos)