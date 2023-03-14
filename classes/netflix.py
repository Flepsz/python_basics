
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        if plano in self.planos:
            self.plano = plano
        else:
            self.plano = ''
            print('Plano inválido.')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano = novo_plano
        else:
            print('Plano inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == 'premium' or self.plano == plano_filme:
            print('O cliente {} pode assistir o filme {}'.format(self.nome, filme))
        elif self.plano == 'medium' and plano_filme == 'basic':
            print('O cliente {} pode assistir o filme {}'.format(self.nome, filme))
        else:
            print('O cliente {} pode assistir o filme {}'.format(self.nome, filme))


