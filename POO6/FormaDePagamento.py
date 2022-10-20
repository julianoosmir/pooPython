from enum import Enum

class FormaDePagamento(Enum):
	DEBITO = 'debito'
	CREDITO = 'credito'
	DINHEIRO = 'dinheiro'
	def __str__(self):
	   return self.name


