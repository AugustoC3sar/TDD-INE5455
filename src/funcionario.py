class Funcionario:
    def __init__(self, nome:str, cpf:str, cargo:str, salario:float):
        self.__nome = nome
        self.__cpf = cpf
        self.__cargo = cargo
        self.__salario = salario
        self.__ocorrencias = []

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario

    @property
    def ocorrencias(self):
        return self.__ocorrencias
    
    def adicionarOcorrencia(self, ocorrencia):
        if ocorrencia not in self.__ocorrencias:
            self.__ocorrencias.append(ocorrencia)

    def removerOcorrencia(self, id_ocorrencia):
        for ocorrencia in self.__ocorrencias:
            if (ocorrencia.id == id_ocorrencia):
                self.__ocorrencias.remove(ocorrencia)
