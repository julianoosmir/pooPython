from FormaDePagamento import FormaDePagamento
from Produto import Produto
from Estoque import Estoque
from ProdutoPedido import ProdutoPedido
from functools import reduce

produto1 = Produto(1, "banana")
produto2 = Produto(2, "maca")
produto3 = Produto(3, "pera")

produtosEstoques = [
    Estoque(produto1, 10),
    Estoque(produto2, 20),
    Estoque(produto3, 30)
]

pedidos = []

print("\n produtos no estoque :", produtosEstoques)

def subtrairQuantidade(estoque: Estoque, sub: int):
    estoque.quantidade = estoque.quantidade - sub
    return estoque

def validarEntradas(nome, quantidade):
    validos = [x.iten for x in produtosEstoques if x.iten.nome == nome.strip() and quantidade < x.quantidade]
    if len(validos) <= 0:
      print("digite nome e quantidade corretas")
      return False
    else:
     return True



def fazerCompras():
    global produtosEstoques
    print("faça o pedido")
    nome = input(" o nome do produto ")
    quantidade = int(input("quantidade "))
    if (validarEntradas(nome,quantidade)) :
         produtoCompra: Produto = [x.iten for x in produtosEstoques if x.iten.nome == nome.strip()][0]
         pedidos.append(ProdutoPedido(produtoCompra, quantidade))
         produtosEstoques = [subtrairQuantidade(x, quantidade) for x in produtosEstoques]
    else:
        fazerCompras()
    continuar = int(input("digite 1 para fazer outra compra "))
    if continuar == 1:
        fazerCompras()
def total(pedidos):
    return reduce(lambda a, b: a + (b.iten.preco * b.quantidade), pedidos, 0)
def formaPagamento(forma):
	return [x.name for x in FormaDePagamento if x.name.upper() == forma.upper()]

fazerCompras()

print("\n pedidos : ", pedidos)

print("\n produtos no estoque :", produtosEstoques)

forma = input("total da compra : " + str(total(pedidos)) + " forma de pagamento "+ [x.name for x in FormaDePagamento].__str__() + " ? ")



print("\n","Pedidos: ", pedidos, "total da compra  :", total(pedidos), "forma de pagamento",formaPagamento(forma))

