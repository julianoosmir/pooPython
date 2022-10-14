import random
import fakeDB 

numerosSorteados = []

def sortearNumeros():
    num = random.randint(1, 53)
    if num not in numerosSorteados:
        numerosSorteados.append(num)

for i in range(5):
    sortearNumeros()
    
for i in numerosSorteados:
    print(fakeDB.listaDefuncinarios[i])

