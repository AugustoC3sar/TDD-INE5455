import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa()

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
        # Employee must have name, cpf, role and salary
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(1, len(self.empresa.funcionarios))
        
if __name__ == '__main__':
    unittest.main()