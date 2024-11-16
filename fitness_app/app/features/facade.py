from app.features.calorias.calculo_calorias_diarias  import calcular_gasto_calorico_diario
from app.features.imc.calculo_imc import calcular_imc
from app.features.agua.recomendacao_agua import calcular_recomendacao_agua


class Facade:
    def calcular_gasto_calorico_diario(self, peso, altura, idade, genero, atividade):
        return calcular_gasto_calorico_diario(peso, altura, idade, genero, atividade)

    def calcular_imc(self, peso, altura):
        return calcular_imc(peso, altura)

    def calcular_recomendacao_agua(self, peso):
        return calcular_recomendacao_agua(peso)