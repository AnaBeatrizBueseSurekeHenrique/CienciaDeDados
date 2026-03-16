class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
    def venda(self, val):
        self.estoque -= val
    def repor(self, val):
        self.estoque += val
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}")