class Contato:
    def __init__(self, celular: str, telefone: str, nome: str):
        self.celular = celular
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return "%s%s%s%s%s%s%s%s" % ("\n", "nome : ", self.nome, " | telefone : ", self.telefone,
                                     " | celular: ", self.celular, "\n")
