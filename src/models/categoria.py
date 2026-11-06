class categoria:

    #Definindo atributos
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome

#Definindo metodos para renomear

    def renomear(self, nome):
        self.__nome = nome.strip()
#incluindo regra de negocio

        if nome == "":
            raise ValueError("O nome não pode ser vazio.")

        def __str__(self):
            return f"Categoria: {self.__nome}"
        
