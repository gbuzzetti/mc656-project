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
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 0), 1866.36, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('mulher', 55, 165, 1), 1460.8, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 100), 1296.36, delta=0.1)
    
    # Análise de valor limite - Altura
    def test_calcular_TMB_boundary_height(self):
        self.assertAlmostEqual(calcular_TMB('homem', 70, 50, 23), 1135.26, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('mulher', 70, 250, 23), 1767.7, delta=0.1)
    
    # Análise de valor limite - Peso
    def test_calcular_TMB_boundary_weight(self):
        self.assertAlmostEqual(calcular_TMB('homem', 30, 175, 23), 1199.26, delta=0.1)
        self.assertAlmostEqual(calcular_TMB('mulher', 300, 175, 23), 3651.2, delta=0.1)
    
    # Classes de Equivalência - Partições válidas
    def test_calcular_NA_valid_partitions(self):
        tmb = 1735.3
        valid_levels = ['sedentário', 'levemente ativo', 'moderadamente ativo', 'altamente ativo', 'muito ativo']
        expected_results = [2082.36, 2386.04, 2689.72, 2993.39, 3297.07]
        
        for level, expected in zip(valid_levels, expected_results):
            self.assertAlmostEqual(calcular_NA(tmb, level), expected, delta=0.1)
    
    # Classes de Equivalência - Partições inválidas
    def test_calcular_NA_invalid_partitions(self):
        tmb = 1735.3
        invalid_levels = ['extremely active', '', None, 123, True]
        
        for invalid_level in invalid_levels:
            with self.assertRaises(ValueError):
                calcular_NA(tmb, invalid_level)

    # Testando o cálculo completo do Gasto Calórico Diário (GCD)
    def test_calcular_gasto_calorico_diario_homem(self):
        self.assertEqual(calcular_gasto_calorico_diario('homem', 70, 175, 23, 'moderadamente ativo'), 2690)
    
    def test_calcular_gasto_calorico_diario_mulher(self):
        self.assertEqual(calcular_gasto_calorico_diario('mulher', 55, 165, 20, 'altamente ativo'), 2379)
    
    # Testando exceções para entrada inválida em calcular_gasto_calorico_diario
    def test_calcular_gasto_calorico_diario_sexo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_gasto_calorico_diario('alien', 70, 175, 23, 'moderadamente ativo')

    def test_calcular_gasto_calorico_diario_nivel_invalido(self):
        with self.assertRaises(ValueError):
            calcular_gasto_calorico_diario('mulher', 70, 175, 23, 'inativo extremo')