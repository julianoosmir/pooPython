import fakeDB 

#print(fakeDB.listaDefuncinarios)

nome = input(" digite nome : ")

funiconariosfiltrados = list(filter(lambda x : nome.upper() in x.nome.upper(),fakeDB.listaDefuncinarios))

print(funiconariosfiltrados)