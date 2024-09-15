# Função para calcular o IMC
def calcular_imc(altura: float, peso: float) -> str:
    if altura <= 0 or peso <= 0:
        return "Dados inválidos para cálculo do IMC."
    
    imc = peso / (altura ** 2)
    
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

# Função para calcular a classificação de gordura corporal com base no sexo
def classificar_gordura(gordura: float, sexo: str) -> str:
    sexo = sexo.lower()
    if gordura < 0 or sexo not in ['homem', 'mulher']:
        return "Dados inválidos para classificação de gordura corporal."
    
    if sexo == 'homem':
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
    elif sexo == 'mulher':
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

# Função de validação de dados
def validar_dados_imc(altura: float, peso: float) -> bool:
    return altura > 0 and peso > 0

def validar_dados_gordura(gordura: float, sexo: str) -> bool:
    return gordura >= 0 and sexo.lower() in ['homem', 'mulher']

# so pra saber se o basico ta funcionando,fazer testes mais robustos...
def teste_calcular_imc():
    assert calcular_imc(1.75, 68) == "Peso normal", "Teste IMC falhou!"
    assert calcular_imc(1.60, 45) == "Abaixo do peso", "Teste IMC falhou!"
    assert calcular_imc(1.80, 90) == "Sobrepeso", "Teste IMC falhou!"
    assert calcular_imc(1.50, 100) == "Obesidade Grau III", "Teste IMC falhou!"
    print("Todos os testes de IMC passaram!")

def teste_classificar_gordura():
    assert classificar_gordura(15, "homem") == "Boa forma (fitness)", "Teste Gordura Homem falhou!"
    assert classificar_gordura(35, "mulher") == "Sobrepeso", "Teste Gordura Mulher falhou!"
    assert classificar_gordura(25, "homem") == "Sobrepeso", "Teste Gordura Homem falhou!"
    assert classificar_gordura(12, "mulher") == "Gordura essencial", "Teste Gordura Mulher falhou!"
    print("Todos os testes de Gordura Corporal passaram!")

# Executando os testes
if __name__ == "__main__":
    teste_calcular_imc()
    teste_classificar_gordura()
