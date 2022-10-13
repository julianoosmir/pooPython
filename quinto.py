import fakeDB 

#print(fakeDB.listaDefuncinarios)

sobrenome = input(" digite nome : ")

funiconariosfiltrados = list(filter(lambda x : sobrenome.upper() in x.sobrenome.upper(),fakeDB.listaDefuncinarios))

print(funiconariosfiltrados)