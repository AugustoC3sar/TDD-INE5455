import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.projeto import Projeto
from src.funcionario import Funcionario
from src.ocorrencia import Ocorrencia


class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.gerente = Funcionario("Fábio", "123.456.789-50", "Gerente", 5250.0)
        self.projeto = Projeto(1, "Projeto 1", 50000, "2024-05-30", self.gerente, [])

    '''
        Teste 19
    '''
    def test_criar_projeto(self):
        # Exercise SUT
        projeto = Projeto(2, "Projeto 2", 750000, "2025-05-15", self.gerente, [])
        # Result Verification
        self.assertEqual(projeto.id, 2)
        self.assertEqual(projeto.titulo, "Projeto 2")
        self.assertEqual(projeto.custo, 750000)
        self.assertEqual(projeto.prazo, "2025-05-15")
        self.assertEqual(projeto.gerente, self.gerente)
        self.assertListEqual(projeto.equipe, [self.gerente])

    '''
        Teste 20
    '''
    def test_adicionar_funcionario_a_equipe(self):
        # Inline Setup
        funcionario = Funcionario("Jonas", "345.678.901-10", "Analista", 2500)

        # Exercise SUT
        self.projeto.adicionarAEquipe(funcionario)

        # Result Verification
        self.assertListEqual(self.projeto.equipe, [self.gerente, funcionario])
    
    '''
        Teste 24
    '''
    def test_criar_ocorrencia(self):
        # Inline Setup
        funcionario = Funcionario("Jonas", "345.678.901-10", "Analista", 2500)
        self.projeto.adicionarAEquipe(funcionario)

        # Exercise SUT
        ocorrencia = self.projeto.criarOcorrencia("Revisão dos Requisitos Funcionais", funcionario, "tarefa", 3)

        # Result verification
        self.assertListEqual(self.projeto.ocorrencias, [ocorrencia])


    '''
        Teste 30
    '''
    def test_criar_ocorrencia_funcionario_fora_da_equipe(self):
        # Inline Setup
        funcionario = Funcionario("Jonas", "345.678.901-10", "Analista", 2500)
        
        # Exercise SUT + Result Verification
        with self.assertRaises(ValueError):
            self.projeto.criarOcorrencia("Revisão dos Requisitos Funcionais", funcionario, "tarefa", 3)
    
    '''
        Teste 31
    '''
    def test_encontrar_ocorrencia(self):
        # Inline Setup
        funcionario = Funcionario("Jonas", "345.678.901-10", "Analista", 2500)
        self.projeto.adicionarAEquipe(funcionario)
        ocorrencia = self.projeto.criarOcorrencia("Revisão dos Requisitos Funcionais", funcionario, "tarefa", 3)

        # Exercise SUT
        ocorrencia_ret = self.projeto.encontrarOcorrencia(ocorrencia.id)

        # Result Verification
        self.assertEqual(ocorrencia, ocorrencia_ret)

    '''
        Teste 32
    '''
    def test_encontrar_ocorrencia_inexistente(self):
        # Exercise SUT
        ocorrencia_ret = self.projeto.encontrarOcorrencia(1)

        # Result Verification
        self.assertIsNone(ocorrencia_ret)

    '''
        Teste 33
    '''
    def test_finalizar_ocorrencia(self):
        # Inline Setup
        funcionario = Funcionario("Jonas", "345.678.901-10", "Analista", 2500)
        self.projeto.adicionarAEquipe(funcionario)
        ocorrencia = self.projeto.criarOcorrencia("Revisão dos Requisitos Funcionais", funcionario, "tarefa", 3)

        # Exercise SUT
        self.projeto.finalizarOcorrencia(ocorrencia.id)

        # Result Verification
        self.assertListEqual(self.projeto.ocorrencias, [])
        self.assertListEqual(ocorrencia.responsavel.ocorrencias, [])
