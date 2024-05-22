import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ocorrencia import Ocorrencia
from src.funcionario import Funcionario

import unittest


class TestOcorrencia(unittest.TestCase):
    def setUp(self):
        self.responsavel = Funcionario("João", "145.689.023.45", "Analista de Redes", 3255.0)
    
    '''
        Teste 22
    '''
    def test_criar_ocorrencia(self):
        # Exercise SUT
        ocorrencia = Ocorrencia(1, "Troca dos switches", self.responsavel, "tarefa", 3)

        # Result Verification
        self.assertEqual(ocorrencia.id, 1)
        self.assertEqual(ocorrencia.resumo, "Troca dos switches")
        self.assertEqual(ocorrencia.responsavel, self.responsavel)
        self.assertEqual(ocorrencia.tipo, "tarefa")
        self.assertEqual(ocorrencia.prioridade, 3)
        self.assertEqual(ocorrencia.estado, 1)

    '''
        Teste 23
    '''
    def test_finalizar_ocorrencia(self):
        # Inline Setup
        ocorrencia = Ocorrencia(1, "Troca dos switches", self.responsavel, "tarefa", 3)

        # Exercise SUT
        ocorrencia.finalizarOcorrencia()

        # Result Verification
        self.assertEqual(ocorrencia.estado, 0)