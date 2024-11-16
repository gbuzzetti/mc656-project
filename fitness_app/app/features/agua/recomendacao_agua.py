recomendacao_agua.py

from typing import Tuple, Optional

def calcular_recomendacao_agua(peso: float) -> Optional[Tuple[float, int]]:

    # Error handling
    if not isinstance(peso, (int, float)) or peso <= 1:
        print('Peso inválido: o peso precisa ser maior que 1!')
        return None

    # Calculo
    qtd_agua = peso * 0.035
    n_copos = qtd_agua / 0.25
    return round(qtd_agua, 1), round(n_copos)