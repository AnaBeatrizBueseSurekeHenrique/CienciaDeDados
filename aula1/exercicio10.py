class Veiculo:
    def __init__(self, nome):
        self.nome = nome
    def tipo_habilitacao(self):
        print('O tipo de habilitação é')
class Moto(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
    def tipo_habilitacao(self):
        print('Tipo: moto')
class Moto(Veiculo):
    def __init__(self, nome):
        super().__init__(nome)
    def tipo_habilitacao(self):
        print('Tipo: carro')