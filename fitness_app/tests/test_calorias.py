import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.features.calorias.calculo_calorias_diarias import calcular_TMB, calcular_NA, calcular_gasto_calorico_diario

class TestCalculoMetabolismo(unittest.TestCase):

    # Classes de Equivalência - Partições válidas
    def test_calcular_TMB_valid_partitions(self):
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 23), 1735.3, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('mulher', 55, 165, 20), 1379.1, delta=0.1)
    
    # Classes de Equivalência - Partições inválidas
    def test_calcular_TMB_invalid_partitions(self):
        invalid_inputs = ['alien', None, 123, '', True]
        for invalid_input in invalid_inputs:
            with self.assertRaises(ValueError):
                calcular_TMB(invalid_input, 70, 175, 23)
    
    # Análise de valor limite - Idade
    def test_calcular_TMB_boundary_age(self):
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 0), 1794.36, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 1), 1788.66, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 100), 1185.36, delta=0.1)
    
    # Análise de valor limite - Altura
    def test_calcular_TMB_boundary_height(self):
        self.assertAlmostEqual(calcular_TMB('homem', 70, 50, 23), 1415.3, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('homem', 70, 250, 23), 2335.3, delta=0.1)
    
    # Análise de valor limite - Peso
    def test_calcular_TMB_boundary_weight(self):
        self.assertAlmostEqual(calcular_TMB('homem', 30, 175, 23), 1331.3, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('homem', 300, 175, 23), 5287.3, delta=0.1)
    
    # Classes de Equivalência - Partições válidas
    def test_calcular_NA_valid_partitions(self):
        tmb = 1735.3
        valid_levels = ['sedentário', 'levemente ativo', 'moderadamente ativo', 'altamente ativo', 'muito ativo']
        expected_results = [2082.36, 2386.54, 2689.72, 2992.87, 3296.07]
        
        for level, expected in zip(valid_levels, expected_results):
            self.assertAlmostEqual(calcular_NA(tmb, level), expected, delta=0.1)
    
    # Classes de Equivalência - Partições inválidas
    def test_calcular_NA_invalid_partitions(self):
        tmb = 1735.3
        invalid_levels = ['extremely active', '', None, 123, True]
        
        for invalid_level in invalid_levels:
            with self.assertRaises(ValueError):
                calcular_NA(tmb, invalid_level)