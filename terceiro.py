import fakeDB

sexo = input(" digite sexo M para masculino e F para Feminio : ")
print(sexo == 'm' or  sexo == 'f')
if not sexo == 'm' and not sexo == 'f':
    print("digite valor valido")
else:
    funiconariosfiltrados = list(filter(lambda x : sexo in x.sexo,fakeDB.listaDefuncinarios))
    print(funiconariosfiltrados)