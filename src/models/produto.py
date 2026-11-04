# classe produto

#definindo a classe produto
class Produto:

    #Definindo atributos e privacidade
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = 2.0
        self.__estoque = 0

#definindo metodo Regra RN1 alterar preço de outra(chamar outra função)  
        self.alterar_preco(preco)
        if preco < 0:
            print ("Preço não pode ser negativo")

            self.baixar_estoque(estoque)
            if estoque < 0:
                print ("Estoque não pode ser negativo")

                self.repor_estoque(estoque)


    def alterar_preco(self, valor):
        if valor < 0:
            print ("Preço invalido")
        self.__preco = float (valor)

    def baixar_estoque(self, quantidade):
        if quantidade < 0:
            print ("Não tem estoque")
        self.__estoque = int (quantidade)