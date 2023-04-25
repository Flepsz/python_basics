
class ControleRemoto:
    def __init__(self, valorcor, altura, prof, largura):
        self.cor = valorcor
        self.altura = altura
        self.prof = prof
        self.largura = largura

    def passarcanal(self, botao):
        if botao == '+':
            print('Próximo canal')
        elif botao == '-':
            print('Canal anterior')
