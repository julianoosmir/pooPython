from datetime import date
import random
import json
from Funcionario import Funcionario

with open("nomes.txt","r",encoding="utf-8") as nomes:
    listaNomes  = nomes.readlines()
    listaNomes = [x.replace(" ","") for x in listaNomes]

with open("sobrenomes.txt","r",encoding="utf-8") as sobrenomes:
    listaSobrenomes = sobrenomes.readlines()
    listaSobrenomes = [x.replace(" ","") for x in listaSobrenomes]

with open("datas.txt","r",encoding="utf-8") as datas:
    listadatas = datas.readlines()
    listadatas = [x.replace(" ","") for x in listadatas]

print(listadatas)



listafunc : list = []
datas = []
for i in range(53):
    ano = random.randint(1990,2000)
    mes = random.randint(1,12)
    dia = random.randint(1,20)
    funcio = Funcionario(i,listaNomes[i],listaSobrenomes[i],date(ano,mes,dia))
    listafunc.append(funcio)
      
for i in range(53):
    ano = random.randint(1990,2000)
    mes = random.randint(1,12)
    dia = random.randint(1,20)
    
    datas.append(date(ano,mes,dia).strftime("%d/%m/%Y"))


with open("datas.txt", 'w') as f:
    f.write("{}".format(datas))
