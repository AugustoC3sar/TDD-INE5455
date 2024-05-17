import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa('Empresa 1')

    '''
        Teste 1
    '''
    def test_criar_empresa(self):
        # Inline Fixture Setup
        nome_empresa = 'Empresa 1'
        # Exercise SUT
        empresa = Empresa(nome_empresa)
        # Result Verification
        self.assertEqual(nome_empresa, empresa.nome)

    '''
        Teste 2
    '''
    def test_cadastrar_funcionario(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(1, len(self.empresa.funcionarios))

    '''
        Teste 3
    '''
    def test_cadastrar_funcionario_nome_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario(123, '12345678900', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Nome inválido.")

    '''
        Teste 4
    '''
    def test_cadastrar_funcionario_cpf_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as e:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(e.exception.args[0], "CPF inválido.")

    '''
        Teste 5
    '''
    def test_cadastrar_funcionario_cargo_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 123, 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Cargo inválido.")

    '''
        Teste 6
    '''
    def test_cadastrar_funcionario_salario_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 'Gerente', 1000)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Salário inválido.")

    '''
        Teste 7
    '''
    def test_cadastrar_dois_funcionarios(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        self.empresa.cadastrarFuncionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(2, len(self.empresa.funcionarios))

    '''
        Teste 8
    '''
    def test_cadastrar_funcionario_que_ja_esta_cadastrado(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Funcionário já cadastrado.")

    '''
        Teste 9
    '''
    def teste_encontra_funcionario_registrado(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        cpf = '123.456.789-00'
        self.empresa.cadastrarFuncionario('Fulano', cpf, 'Gerente', 1000.0)
        # Exercise SUT
        funcionario = self.empresa.encontrarFuncionario('123.456.789-00')
        # Result Verification
        self.assertEqual(cpf, funcionario[1])

    '''
        Teste 10
    '''
    def teste_nao_encontra_funcionario_nao_registrado(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.encontrarFuncionario('123.456.789-00')
        # Result Verification
        self.assertEqual(error.exception.args[0], "Funcionário não encontrado.")

        
if __name__ == '__main__':
    unittest.main()