import re
from typing import List

class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def funcionarios(self):
        return self.__funcionarios
    
    def cadastrarFuncionario(self, nome: str, cpf: str, cargo: str, salario: float):           
        self.__funcionarios.append((nome, cpf, cargo, salario))