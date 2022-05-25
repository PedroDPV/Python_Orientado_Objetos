"""USAREMOS AGREGAÇÃO QUANDO UMA CLASSE PRECISAR DE OUTRA CLASSE DIFERENTE PRA UM FUNCIONAMENTO CORRETO"""

class CarrinhoDeCompras:  #A Classe CarrinhoDeCompras , varias vezes irá necessitar da classe Produto
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append((produto))

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return print(f'R${total:.2f}')


class Produto:   # Porém a classe Produto é independete do carrinho de compras
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



carrinho = CarrinhoDeCompras()


produto1 = Produto('camiseta', 50)
produto2 = Produto('iphone', 3000)
produto3 = Produto('caneca', 10)



carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)
carrinho.inserir_produto(produto3)
carrinho.inserir_produto(produto1)
carrinho.inserir_produto(produto2)

carrinho.lista_produto()
carrinho.soma_total()