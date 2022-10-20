from .ProdutoPedido import ProdutoPedido
from .FormaDePagamento import FormaDePagamento
class Venda:
    def __init__(self,pedidos: list(ProdutoPedido),formaDePagamento: FormaDePagamento):
        self.pedidos = pedidos
        self.formaDePagamento = formaDePagamento


