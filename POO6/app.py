from Produto import Produto
from Estoque import Estoque
from ProdutoPedido import ProdutoPedido

produto1 = Produto(1,"banana")
produto2 = Produto(2,"maca")
produto3 = Produto(3,"pera")

produtosEstoques = [
    Estoque(produto1,10),
    Estoque(produto2,20),
    Estoque(produto3,30)
]

pedidos = []

print(produtosEstoques)

def subtrairQuantidade(estoque : Estoque,sub : int):
    estoque.quantidade = estoque.quantidade - sub
    return estoque

def fazerCompras():
    global produtosEstoques
    print("faça o pedido")
    nome = input(" o nome do produto ")
    quantidade = int(input("quantidade "))
    produtoCompra: Produto = [x.iten for x in produtosEstoques if x.iten.nome == nome][0]
    pedidos.append(ProdutoPedido(produtoCompra,quantidade))
    produtosEstoques = [subtrairQuantidade(x,quantidade) for x in produtosEstoques]

    continuar = int(input("digite 1 para fazer outra compra"))
    if continuar == 1:
        fazerCompras()

fazerCompras()

print(pedidos)

print(produtosEstoques)


