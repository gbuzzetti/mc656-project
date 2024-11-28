# test_saude.py
import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.features.imc.calculo_imc import calcular_imc, classificar_gordura, classificar_imc

class TestFitnessFunctions(unittest.TestCase):
    
    # Testes para a função calcular_imc
    def test_calcular_imc_abaixo_do_peso(self):
        """ Testa o cálculo de IMC para o resultado 'Abaixo do peso' """
        self.assertEqual(calcular_imc(1.75, 50), ("Abaixo do peso", 16.33))
    
    def test_calcular_imc_peso_normal(self):
        """ Testa o cálculo de IMC para o resultado 'Peso normal' """
        self.assertEqual(calcular_imc(1.75, 68), ("Peso normal", 22.20))
    
    def test_calcular_imc_sobrepeso(self):
        """ Testa o cálculo de IMC para o resultado 'Sobrepeso' """
        self.assertEqual(calcular_imc(1.75, 80), ("Sobrepeso", 26.12))
    
    def test_calcular_imc_obesidade_grau_I(self):
        """ Testa o cálculo de IMC para o resultado 'Obesidade Grau I' """
        self.assertEqual(calcular_imc(1.75, 95), ("Obesidade Grau I", 31.02))
    
    def test_calcular_imc_obesidade_grau_II(self):
        """ Testa o cálculo de IMC para o resultado 'Obesidade Grau II' """
        self.assertEqual(calcular_imc(1.75, 110), ("Obesidade Grau II", 35.92))
    
    def test_calcular_imc_obesidade_grau_III(self):
        """ Testa o cálculo de IMC para o resultado 'Obesidade Grau III' """
        self.assertEqual(calcular_imc(1.75, 125), ("Obesidade Grau III", 40.82))
    
    def test_calcular_imc_dados_invalidos(self):
        """ Testa se a função retorna mensagem de erro para valores inválidos """
        self.assertEqual(calcular_imc(0, 70), "Dados inválidos para cálculo do IMC.")
        self.assertEqual(calcular_imc(1.75, 0), "Dados inválidos para cálculo do IMC.")
        self.assertEqual(calcular_imc(-1.75, 70), "Dados inválidos para cálculo do IMC.")
    
    # Testes para a função classificar_gordura
    def test_classificar_gordura_essencial_homem(self):
        """ Testa classificação de gordura 'Gordura essencial' para homem """
        self.assertEqual(classificar_gordura(3, 'homem'), "Gordura essencial")
    
    def test_classificar_gordura_atleta_homem(self):
        """ Testa classificação de gordura 'Atleta' para homem """
        self.assertEqual(classificar_gordura(10, 'homem'), "Atleta")
    
    def test_classificar_gordura_fitness_homem(self):
        """ Testa classificação de gordura 'Boa forma (fitness)' para homem """
        self.assertEqual(classificar_gordura(15, 'homem'), "Boa forma (fitness)")
    
    def test_classificar_gordura_aceitavel_homem(self):
        """ Testa classificação de gordura 'Aceitável' para homem """
        self.assertEqual(classificar_gordura(20, 'homem'), "Aceitável")
    
    def test_classificar_gordura_sobrepeso_homem(self):
        """ Testa classificação de gordura 'Sobrepeso' para homem """
        self.assertEqual(classificar_gordura(27, 'homem'), "Sobrepeso")
    
    def test_classificar_gordura_obesidade_homem(self):
        """ Testa classificação de gordura 'Obesidade' para homem """
        self.assertEqual(classificar_gordura(32, 'homem'), "Obesidade")
    
    def test_classificar_gordura_essencial_mulher(self):
        """ Testa classificação de gordura 'Gordura essencial' para mulher """
        self.assertEqual(classificar_gordura(12, 'mulher'), "Gordura essencial")
    
    def test_classificar_gordura_atleta_mulher(self):
        """ Testa classificação de gordura 'Atleta' para mulher """
        self.assertEqual(classificar_gordura(15, 'mulher'), "Atleta")
    
    def test_classificar_gordura_fitness_mulher(self):
        """ Testa classificação de gordura 'Boa forma (fitness)' para mulher """
        self.assertEqual(classificar_gordura(22, 'mulher'), "Boa forma (fitness)")
    
    def test_classificar_gordura_aceitavel_mulher(self):
        """ Testa classificação de gordura 'Aceitável' para mulher """
        self.assertEqual(classificar_gordura(28, 'mulher'), "Aceitável")
    
    def test_classificar_gordura_sobrepeso_mulher(self):
        """ Testa classificação de gordura 'Sobrepeso' para mulher """
        self.assertEqual(classificar_gordura(35, 'mulher'), "Sobrepeso")
    
    def test_classificar_gordura_obesidade_mulher(self):
        """ Testa classificação de gordura 'Obesidade' para mulher """
        self.assertEqual(classificar_gordura(42, 'mulher'), "Obesidade")
    
    def test_classificar_gordura_dados_invalidos(self):
        """ Testa se a função retorna mensagem de erro para valores inválidos """
        self.assertEqual(classificar_gordura(-5, 'homem'), "Dados inválidos para classificação de gordura corporal.")
        self.assertEqual(classificar_gordura(15, 'alien'), "Dados inválidos para classificação de gordura corporal.")

    # TESTES DA A5

    def test_classificar_imc_particionamento(self):
        """ Testa classificação de IMC com critérios de particionamento """
        self.assertEqual(classificar_imc(18.4), "Abaixo do peso")
        self.assertEqual(classificar_imc(18.5), "Peso normal")
        self.assertEqual(classificar_imc(24.9), "Peso normal")
        self.assertEqual(classificar_imc(25.0), "Sobrepeso")
        self.assertEqual(classificar_imc(29.9), "Sobrepeso")
        self.assertEqual(classificar_imc(30.0), "Obesidade Grau I")

    def test_calcular_imc_analise_valor_limite(self):
    """ Testa cálculo de IMC com critérios de análise de valor limite """
    self.assertEqual(calcular_imc(1.75, 70), ("Peso normal", 22.86))
    self.assertEqual(calcular_imc(1.60, 100), ("Obesidade Grau II", 39.06))  # Corrigido
    self.assertEqual(calcular_imc(0, 70), "Dados inválidos para cálculo do IMC.")


    def test_classificar_gordura_particionamento(self):
        """ Testa classificação de gordura corporal com particionamento """
        self.assertEqual(classificar_gordura(3, "homem"), "Gordura essencial")
        self.assertEqual(classificar_gordura(15, "mulher"), "Atleta")
        self.assertEqual(classificar_gordura(-5, "mulher"), "Dados inválidos para classificação de gordura corporal.")

if __name__ == '__main__':
    unittest.main()
