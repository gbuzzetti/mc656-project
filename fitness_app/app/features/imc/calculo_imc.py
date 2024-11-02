from typing import Tuple


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"


def calcular_imc(altura: float, peso: float) -> Tuple[str, float]:
    if altura <= 0 or peso <= 0:
        return "Dados inválidos para cálculo do IMC.", 0.0
    imc = peso / (altura ** 2)
    classificacao = classificar_imc(imc)
    return classificacao, round(imc, 2)



def classificar_gordura_homem(gordura: float) -> str:
    if 2 <= gordura <= 5:
        return "Gordura essencial"
    elif 6 <= gordura <= 13:
        return "Atleta"
    elif 14 <= gordura <= 17:
        return "Boa forma (fitness)"
    elif 18 <= gordura <= 24:
        return "Aceitável"
    elif 25 <= gordura <= 29:
        return "Sobrepeso"
    else:
        return "Obesidade"

def classificar_gordura_mulher(gordura: float) -> str:
    if 10 <= gordura <= 13:
        return "Gordura essencial"
    elif 14 <= gordura <= 20:
        return "Atleta"
    elif 21 <= gordura <= 24:
        return "Boa forma (fitness)"
    elif 25 <= gordura <= 31:
        return "Aceitável"
    elif 32 <= gordura <= 39:
        return "Sobrepeso"
    else:
        return "Obesidade"

def classificar_gordura(gordura: float, sexo: str) -> str:
    sexo = sexo.lower()
    if gordura < 0 or sexo not in ['homem', 'mulher']:
        return "Dados inválidos para classificação de gordura corporal."
    
    if sexo == 'homem':
        return classificar_gordura_homem(gordura)
    elif sexo == 'mulher':
        return classificar_gordura_mulher(gordura)
