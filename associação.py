"""Vamos criar 3 classes diferentes que a princípio não possuem nenhum vínculo uma com a outra """


class Escritor:
    def __init__(self, nome, idade):
        self.__nome = nome    # ao colocarmos dois UNDERLINES antes da variavel estaremos privando(a) , uma forma de acessa-la será fazendo um Getter-Setter posteriormente
        self.idade = idade
        self.__ferramenta = None # a ferramenta com atributo none , quer dizer que ela irá reproduzir apenas oq for designado a ela por outras classes

    @property               # <- Getter para quando recebermos o parametro (nome) linkar á variável privada no caso o "__nome"
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter   # estamos dizendo que a nossa ferramenta será associada ao que for passado no parametro dela
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('a caneta está escrevendo...')



class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')


"""Primeiramente vamos chamar as funções de cada classe normalmente"""
escritor = Escritor('Pedro', 27)
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(f'\nO escritor {escritor.nome} tem {escritor.idade} anos')
print(caneta.marca)
maquina.escrever()
caneta.escrever()

print('#'*300)
"""Agora chamaremos dentro da classe ESCRITOR , uma função de outras classes no caso as classes : 'Caneta" e 'MaquinaDeEscrever' """
escritor.ferramenta = maquina  # a variável maquina foi associada á classe MaquinaDeEscrever na linha 44, agora nossa ferramenta possui a função de tudo que estiver contido na classe MaquinaDeEscrever
escritor.ferramenta.escrever() #como só existe uma função na Classe que foi associada , chamaremos ela normalmente com o ".escrever()"

