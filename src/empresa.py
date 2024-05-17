import re
from typing import List

class Empresa:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []
        self.__projetos = []
        self.__contadorIdProjeto = 1

    @property
    def nome(self):
        return self.__nome
    
    @property
    def funcionarios(self):
        return self.__funcionarios
    
    @property
    def projetos(self):
        return self.__projetos
    
    @property
    def contadorIdProjeto(self):
        return self.__contadorIdProjeto
    
    @contadorIdProjeto.setter
    def contadorIdProjeto(self, id):
        self.__contadorIdProjeto = id
    
    def __validaCPF(self, cpf: str):
        return bool(re.match(r"^([0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2})$", cpf))
    
    def cadastrarFuncionario(self, nome: str, cpf: str, cargo: str, salario: float):           
        if not isinstance(nome, str):
            raise ValueError("Nome inválido.")
        
        if not isinstance(cargo, str):
            raise ValueError("Cargo inválido.")
        
        if not isinstance(salario, float):
            raise ValueError("Salário inválido.")
        
        if not self.__validaCPF(cpf):
            raise ValueError("CPF inválido.")
        
        for funcionario in self.funcionarios:
            if funcionario[1] == cpf:
                raise ValueError("Funcionário já cadastrado.")
        
        self.__funcionarios.append((nome, cpf, cargo, salario))

    def encontrarFuncionario(self, cpf: str):
        for funcionario in self.funcionarios:
            if funcionario[1] == cpf:
                return funcionario
            
        raise ValueError("Funcionário não encontrado.")
    
    def novoProjeto(self, titulo: str, custo: float, prazo: str, gerente, equipe: []):
        self.__projetos.append((self.contadorIdProjeto, titulo, custo, prazo, gerente, equipe))
        self.contadorIdProjeto += 1