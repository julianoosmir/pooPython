from Contato import Contato
from Agenda import Agenda

contatos = [
    Contato('99999999', '88888', 'jose')
]
agenda = Agenda(contatos)
agenda.mostrarAgenda()