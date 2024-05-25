import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ocorrencia import Ocorrencia
from src.funcionario import Funcionario

import unittest


class TestOcorrencia(unittest.TestCase):
    def setUp(self):
        self.responsavel = Funcionario("João", "145.689.023.45", "Analista de Redes", 3255.0)
        self.ocorrencia = Ocorrencia(1, "Troca dos switches", self.responsavel, "tarefa", 3)
    
    '''
        Teste 22
    '''
    def test_criar_ocorrencia(self):
        # Exercise SUT
        ocorrencia = Ocorrencia(2, "Configuração do Firewall", self.responsavel, "tarefa", 2)

        # Result Verification
        self.assertEqual(ocorrencia.id, 2)
        self.assertEqual(ocorrencia.resumo, "Configuração do Firewall")
        self.assertEqual(ocorrencia.responsavel, self.responsavel)
        self.assertEqual(ocorrencia.tipo, "tarefa")
        self.assertEqual(ocorrencia.prioridade, 2)
        self.assertEqual(ocorrencia.estado, 1)

    '''
        Teste 23
    '''
    def test_finalizar_ocorrencia(self):
        # Implicit setup

        # Exercise SUT
        self.ocorrencia.finalizarOcorrencia()

        # Result Verification
        self.assertEqual(self.ocorrencia.estado, 0)
    
    '''
        Teste 25
    '''
    def test_modificar_prioridade(self):
        # Implicit Setup

        # Exercise SUT
        self.ocorrencia.modificarPrioridade(2)

        # Result Verification
        self.assertEqual(self.ocorrencia.prioridade, 2)

    '''
        Teste 26
    '''
    def test_modificar_prioridade_invalida(self):
        # Implicit Setup

        # Exercise SUT
        with self.assertRaises(ValueError):
            self.ocorrencia.modificarPrioridade(4)
    