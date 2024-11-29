# Funcao para calcular Taxa de Metabolismo Basal
def calcular_TMB(sexo, peso, altura, idade):
    # Input validation
    if not isinstance(sexo, str) or sexo.lower() not in ['homem', 'mulher']:
        raise ValueError("Sexo inválido. Use 'homem' ou 'mulher'.")
    if not isinstance(peso, (int, float)) or not (30 <= peso <= 300):
        raise ValueError("Peso inválido. Deve estar entre 30kg e 300kg.")
    if not isinstance(altura, (int, float)) or not (50 <= altura <= 250):
        raise ValueError("Altura inválida. Deve estar entre 50cm e 250cm.")
    if not isinstance(idade, (int, float)) or not (0 <= idade <= 120):
        raise ValueError("Idade inválida. Deve estar entre 0 e 120 anos.")
    
    # TMB calculation
    if sexo.lower() == 'homem':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif sexo.lower() == 'mulher':
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

    return tmb

# Funcao para ajustar o Nivel de Atividade no Gasto Calorico Diario
def calcular_NA(tmb, nivel_atividade):
    niveis_atividade = {
        'sedentário': 1.2,
        'levemente ativo': 1.375,
        'moderadamente ativo': 1.55,
        'altamente ativo': 1.725,
        'muito ativo': 1.9
    }

    if not isinstance(nivel_atividade, str):
        raise ValueError("Nível de atividade inválido.")
    
    if nivel_atividade.lower() not in niveis_atividade:
        raise ValueError("Nível de atividade inválido.")

    gcd = tmb * niveis_atividade[nivel_atividade.lower()]
    return gcd

def calcular_gasto_calorico_diario(sexo, peso, altura, idade, nivel_atividade):
    tmb = calcular_TMB(sexo, peso, altura, idade)
    gcd = calcular_NA(tmb, nivel_atividade)
    return round(gcd)
