# funcao para calcular Taxa de Metabolismo Basal
def calcular_TMB(sexo, peso, altura, idade):
    if sexo.lower() == 'homem':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif sexo.lower() == 'mulher':
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

    # tratar entrada do sexo, pode ser alterado de acordo com o front-end
    else:
        raise ValueError("Sexo inválido. Use 'homem' ou 'mulher'.")
    return tmb

# funcao para ajustar o Nivel de Atividade no Gasto Calorico Diario
def calcular_NA(tmb, nivel_atividade):
    niveis_atividade = {
        'sedentário': 1.2,
        'levemente ativo': 1.375,
        'moderadamente ativo': 1.55,
        'altamente ativo': 1.725,
        'muito ativo': 1.9
    }
    
    # tratar entrada do nivel de atividade, pode ser alterado de acordo com o front-end
    if nivel_atividade.lower() not in niveis_atividade:
        raise ValueError("Nível de atividade inválido.")
    
    gcd = tmb * niveis_atividade[nivel_atividade.lower()]
    return gcd

def calcular_gasto_calorico_diario(sexo, peso, altura, idade, nivel_atividade):
    tmb = calcular_TMB(sexo, peso, altura, idade)
    gcd = calcular_NA(tmb, nivel_atividade)
    return round(gcd)
