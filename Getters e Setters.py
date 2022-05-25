import re

"""
O GETTER VAI USAR A FUNÇÃO @propierty PARA SE "APROPRIAR" DA VARIAVEL "preco" INFORMADA DE FORMA INCORRETA  E NOS RETORNARÁ UMA ESPÉCIA DE CÓPIA
NO CASO ( _preco ) PARA QUE POSSAMOS MANIPULA-LA SEM AFETAR O RESTANTE DO NOSSO CÓDIGO.

O SETTER VAI USAR A FUNÇÃO @variavel.setter PARA FILTRAR TUDO AQUILO QUE POSSA CAUSAR UM ERRO DE INDICAÇÃO NO PARAMETRO 
E IRÁ SETTAR DEVOLTA NA NOSSA VARIAVEL DE ORIGEM NO CASO "preco" PORÉM AGORA DEVIDAMENTE FILTRADA , RETORNADO UM FLOAT.
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(re.sub(r'[^0-9]', '', valor))
        self._preco = valor


"""
NESTE EXEMPLO USAREMOS O GETTER E O SETTER PARA CORRIGIR ESTE PROBLEMA , PERCEBA QUE MENOS QUE NOSSO PARAMETRO RECEBA UMA INFORMAÇÃO PROBLEMÁTICA 
IREMOS RETORNAR O MESMO VALOR
"""

p1 = Produto('Camisa', 100)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Camisa', 'R$100')  #  <-- FORMA ERRADA DE INDICAR O PARÂMETRO "PRECO" , MAS O GETTER-SETTER IRÁ RETORNAR O VALOR CORRETO
p2.desconto(10)
print(p2.preco)

p3 = Produto('Camisa', '100 Reais')  #  <-- FORMA ERRADA DE INDICAR O PARÂMETRO "PRECO" , MAS O GETTER-SETTER IRÁ RETORNAR O VALOR CORRETO
p3.desconto(10)
print(p3.preco)




