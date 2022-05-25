class Coleção:
    def __init__(self, modelo, ano, vmaxima, cor, batido=False, vendido=False, pilotando=False):
        self.modelo = modelo
        self.ano = ano
        self.vmaxima = vmaxima
        self.cor = cor
        self.pilotando = pilotando
        self.batido =  batido
        self.vendido = vendido

        pass

    def correndo(self, velocidade):
        if self.pilotando == True:
            print(f'a velocidade de {self.modelo} ja foi informada')
            return

        print(f'{self.modelo} está pilotando á {velocidade}km/h')
        self.pilotando = True

    def parar_de_correr(self):
        if self.pilotando == True:
            print(f'{self.modelo} encerrou a corrida e está voltando para a garagem')
            self.pilotando = False
            return
        print(f'{self.modelo} já está na garagem')

    def abastecer(self, litros):
        if self.pilotando == True:
            print(f'{self.modelo} está na estrada e não pode abastecer')
            return
        print(f'Pronto ! o {self.modelo} abasteceu {litros} litros')
        self.pilotando = False

class Pilotos:
    def __init__(self, nome, idade, peso, nivel, contratado=False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.nivel = nivel
        self.contratado = contratado
        pass

    def contratar(self):
        if self.contratado == False:
            print(f'Parabéns {self.nome} [{self.nivel}], você foi contratado !')
            self.contratado = True
            return
        print(f'Desculpe , mas o piloto {self.nome} não está disponível')


piloto1 = Pilotos('Pedro', 27, 70, 10,)
carro1 = Coleção('civic', '2015', 200, 'vermelho', True, False, False)
carro1.modelo = 'Honda civic'

carro1.correndo(250)
carro1.parar_de_correr()
carro1.parar_de_correr()
carro1.correndo(300)
carro1.abastecer(50)
carro1.parar_de_correr()
carro1.abastecer(50)
piloto1.contratar()
piloto1.contratar()




