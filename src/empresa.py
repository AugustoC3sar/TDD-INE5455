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
    
    def __validaCPF(self, cpf: str):
        return bool(re.match(r"^([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2})$", cpf))
    
    def cadastrarFuncionario(self, nome: str, cpf: str, cargo: str, salario: float):           
        if not isinstance(nome, str):
            raise ValueError("Nome inválido.")
        
        if not isinstance(cargo, str):
            raise ValueError("Cargo inválido.")
        
        if not self.__validaCPF(cpf):
            raise ValueError("CPF inválido.")
        
        self.__funcionarios.append((nome, cpf, cargo, salario))
