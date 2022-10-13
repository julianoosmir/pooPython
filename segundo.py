import fakeDB 

ano = int(input(" digite o ano : "))

funiconariosfiltrados = list(filter(lambda x : x.dataNascimento.year == ano,fakeDB.listaDefuncinarios))

for funcionario in funiconariosfiltrados:
	print("{0} {1}".format(funcionario.nome,funcionario.sobrenome))