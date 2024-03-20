import unittest
from io import StringIO
from unittest.mock import patch
import main

class TestCalcularNomina(unittest.TestCase):
    @patch('builtins.input', side_effect=['3000', '100', '1 mes', '2', '3', '4', '5', '10', '10', '10', '6', '7'])
    def test_calcular_nomina_1(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            your_module.calcular_nomina()
            self.assertIn('=== Resultados ===', fake_out.getvalue())

    @patch('builtins.input', side_effect=['4000', '200', '2 meses', '3', '4', '5', '6', '20', '20', '20', '7', '8'])
    def test_calcular_nomina_2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            your_module.calcular_nomina()
            self.assertIn('=== Resultados ===', fake_out.getvalue())

