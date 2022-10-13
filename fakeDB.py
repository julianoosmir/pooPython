from datetime import datetime
from Funcionario import Funcionario

with open("nomes.txt","r",encoding="utf-8") as nomes:
    listaNomes  = nomes.readlines()
    listaNomes = [x.replace(" ","") for x in listaNomes]

with open("sobrenomes.txt","r",encoding="utf-8") as sobrenomes:
    listaSobrenomes = sobrenomes.readlines()
    listaSobrenomes = [x.replace(" ","") for x in listaSobrenomes]

with open("datas.txt","r",encoding="utf-8") as datas:
    listadatas = datas.readlines()
    listadatas = [x.replace("\n","") for x in listadatas]



listaDefuncinarios : list = []
for i in range(53):
    dta = datetime.strptime(listadatas[i],'%m/%d/%Y').date()
    funcio = Funcionario(i,listaNomes[i],listaSobrenomes[i],dta)
    listaDefuncinarios.append(funcio)

