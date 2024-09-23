from typing import Tuple

# def calcular_recomendacao_agua(peso: float) -> Tuple[float, int]: 
def calcular_recomendacao_agua(peso: float): 
    try:
        if peso > 1:
            qtd_agua = peso * 0.035
            # n_copos = qtd_agua / 0.25
            # return  (round(qtd_agua, 1), round(n_copos))
            return round(qtd_agua, 2)
        else:
            print('Peso inválido: o peso precisa ser maior que 1!')
            return None
    
    except Exception as e:
        print(f'Peso inválido: {e}')
        return None
