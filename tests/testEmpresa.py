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
        Teste 3
    '''
    def test_cadastrar_funcionario_cargo_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 123, 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Cargo inválido.")
        
if __name__ == '__main__':
    unittest.main()