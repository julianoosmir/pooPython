import fakeDB 

#print(fakeDB.listaDefuncinarios)

nome = input(" digite 3 letras do  nome : ")

if len(nome) > 3:
    print("digite ate 3 letras")
else:
    funiconariosfiltrados = list(filter(lambda x : nome.upper() in x.nome.upper()[0:3],fakeDB.listaDefuncinarios))
    print(funiconariosfiltrados)