from datetime import datetime


class ContaBancaria:
	def __init__(self):
		self.__saldo : float = 0.0
		self.__dataAbertura : datetime = datetime.now()

	def depositar(self,valor:float):
		self.__saldo += valor

	def sacar(self,valor:float):
		if valor > self.__saldo :
			print("saldo insuficiente")
		else:
			self.__saldo -= valor
			print("saque do valor de R$ {:.2f} liberado".format(valor))
			return valor

	def  ObterSaldoFormatado(self):
		return "%s%.2f" % ("R$ ",self.__saldo)

	def  ObterDataAberturaFormatada(self):
		return self.__dataAbertura.strftime("%d/%m/%Y")


