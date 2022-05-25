class Pessoa:
    def __init__(self,nome ,idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):  # uma função para me mostrar de qual classe ela está sendo executada
        print(f'{self.nomeclasse} está falando...')

class Alunos(Pessoa):
    pass

class Professores(Pessoa):
    pass


a1 = Alunos('pedro', 27)
p1 = Professores('Mayana', 28)

#um objeto de outra classe , está usando todas as funções HERDADAS de uma classe indicada (Pessoa) no parametro de nossas classes filhas na hora da criação

a1.falar()
p1.falar()