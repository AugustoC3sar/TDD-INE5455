import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.empresa import Empresa

class TestEmpresa(unittest.TestCase):
    def run_tests():
        unittest.main()

    def test_criar_empresa(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        nome_empresa = 'Empresa 1'
        # Exercise SUT
        empresa = Empresa(nome_empresa)
        # Result Verification
        self.assertEqual(nome_empresa, empresa.nome)
        
if __name__ == '__main__':
    unittest.main()