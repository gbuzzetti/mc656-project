import unittest
import recomendacao_agua as agua

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

    def test_valid_param(self):
        
        self.assertEqual(agua.calcular_recomendacao_agua(75), (2.6, 11))
        self.assertEqual(agua.calcular_recomendacao_agua(50), (1.8, 7))
        self.assertEqual(agua.calcular_recomendacao_agua(100), (3.5, 14))


if __name__ == '__main__':
    unittest.main()