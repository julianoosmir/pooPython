import fakeDB 

sobrenome = input(" digite 3 letras do  sobrenome : ")

if len(sobrenome) > 3:
    print("digite ate 3 letras")
else:
    funiconariosfiltrados = list(filter(lambda x : sobrenome.upper() in x.sobrenome.upper()[0:3],fakeDB.listaDefuncinarios))
    print(funiconariosfiltrados)