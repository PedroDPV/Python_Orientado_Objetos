class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []


    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self, cidade, estado):
        self.estado = estado
        self.cidade = cidade

cliente1 = Cliente('pedro', 27)
cliente1.insere_endereco('Recife', 'PE')
cliente1.lista_enderecos()


