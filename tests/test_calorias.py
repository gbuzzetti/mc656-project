import unittest
from fitness_app.app.features.calorias.calculo_calorias_diarias import calcular_TMB, calcular_NA, calcular_gasto_calorico_diario

class TestCalculoMetabolismo(unittest.TestCase):
    
    # Testando a função calcular_TMB para homens
    def test_calcular_TMB_homem(self):
        self.assertAlmostEqual(calcular_TMB('homem', 70, 175, 23), 1735.3, delta=0.1)
    
    # Testando a função calcular_TMB para mulheres
    def test_calcular_TMB_mulher(self):
        self.assertAlmostEqual(calcular_TMB('mulher', 55, 165, 20), 1379.1, delta=0.1)

    # Testando exceção para sexo inválido
    def test_calcular_TMB_sexo_invalido(self):
        with self.assertRaises(ValueError):
            calcular_TMB('alien', 70, 175, 23)

    # Testando a função calcular_NA para nível de atividade válido
    def test_calcular_NA_valido(self):
        tmb = 1735.3  # Usando um valor de TMB calculado previamente
        self.assertAlmostEqual(calcular_NA(tmb, 'moderadamente ativo'), 2689.7, delta=0.1)

    # Testando exceção para nível de atividade inválido
    def test_calcular_NA_invalido(self):
        tmb = 1503.4
        with self.assertRaises(ValueError):
            calcular_NA(tmb, 'extremamente ativo')

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
            calcular_gasto_calorico_diario('homem', 70, 175, 23, 'inativo extremo')


if __name__ == '__main__':
    unittest.main()
