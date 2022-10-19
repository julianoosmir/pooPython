from enum import Enum

class FormaDePagamento(Enum):
	DEBITO = 1
	CREDITO = 2 
	DINHEIRO = 3
	def __str__(self):
	   return str(self.value)


print(FormaDePagamento.CREDITO.name)
