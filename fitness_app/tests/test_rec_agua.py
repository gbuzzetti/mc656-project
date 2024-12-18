import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app.features.agua.recomendacao_agua as agua

class TestRecAgua(unittest.TestCase):

    def test_invalid_param(self):
        self.assertIsNone(agua.calcular_recomendacao_agua('Hello'))
        self.assertIsNone(agua.calcular_recomendacao_agua(True))
        self.assertIsNone(agua.calcular_recomendacao_agua(False))
        self.assertIsNone(agua.calcular_recomendacao_agua((1, 2)))
        self.assertIsNone(agua.calcular_recomendacao_agua(0.5))
        self.assertIsNone(agua.calcular_recomendacao_agua(-2))
        self.assertIsNone(agua.calcular_recomendacao_agua([1, 2, 3]))
        self.assertIsNone(agua.calcular_recomendacao_agua({1, 2, 3}))
        self.assertIsNone(agua.calcular_recomendacao_agua({'oi': 1, 'ola': 2}))
        self.assertIsNone(agua.calcular_recomendacao_agua(None))
        #Analise de valor limite - Avaliação 5
        self.assertIsNone(agua.calcular_recomendacao_agua(301))
        self.assertIsNone(agua.calcular_recomendacao_agua(9))

    def test_valid_param(self):
        self.assertEqual(agua.calcular_recomendacao_agua(75), (2.6, 11))
        self.assertEqual(agua.calcular_recomendacao_agua(50), (1.8, 7))
        self.assertEqual(agua.calcular_recomendacao_agua(100), (3.5, 14))
        #Analise de valor limite - Avaliação 5
        self.assertEqual(agua.calcular_recomendacao_agua(300), (10.5, 42))
        self.assertEqual(agua.calcular_recomendacao_agua(10), (0.4, 1))


if __name__ == '__main__':
    unittest.main()