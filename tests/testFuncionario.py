import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia

class TestFuncionario(unittest.TestCase):
    
    def setUp(self):
        self.funcionario = Funcionario("José", "123.456.789-10", "Analista", 2550.0)

    '''
        Teste 18
    '''
    def test_criar_funcionario(self):
        # Exercise SUT
        funcionario = Funcionario("João", "345.678.901-20", "Estagiário", 1200.0)
        # Result Verification
        self.assertEqual(funcionario.nome, "João")
        self.assertEqual(funcionario.cpf, "345.678.901-20")
        self.assertEqual(funcionario.cargo, "Estagiário")
        self.assertEqual(funcionario.salario, 1200.0)
    
    '''
        Teste 28
    '''
    def test_adicionar_ocorrencia(self):
        # Implicit Setup
        # Inline Setup
        ocorrencia = Ocorrencia(1, "Ocorrencia Teste", self.funcionario, "tarefa", 1)

        # Exercise SUT
        self.funcionario.adicionarOcorrencia(ocorrencia)

        # Result Verification
        self.assertListEqual(self.funcionario.ocorrencias, [ocorrencia])
    
    '''
        Teste 29
    '''
    def test_remover_ocorrencia(self):
        # Implicit Setup
        # Inline Setup
        ocorrencia = Ocorrencia(1, "Ocorrencia Teste", self.funcionario, "tarefa", 1)
        self.funcionario.adicionarOcorrencia(ocorrencia)

        # Exercise SUT
        self.funcionario.removerOcorrencia(ocorrencia.id)

        # Result Verification
        self.assertListEqual(self.funcionario.ocorrencias, [])
