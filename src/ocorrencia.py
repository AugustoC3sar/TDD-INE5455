from src.funcionario import Funcionario


class Ocorrencia:
    def __init__(self, id: int, resumo: str, responsavel: Funcionario, tipo: str, prioridade: int):
        self.__id = id
        self.__resumo = resumo
        self.__responsavel = responsavel
        self.__tipo = tipo
        self.__prioridade = prioridade
        self.__estado = 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def resumo(self):
        return self.__resumo

    @property
    def responsavel(self):
        return self.__responsavel
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def prioridade(self):
        return self.__prioridade
    
    @property
    def estado(self):
        return self.__estado

    def finalizarOcorrencia(self):
        self.__estado = 0
    
    def modificarPrioridade(self, prioridade):
        self.__prioridade = prioridade
