from flask import Blueprint, render_template, request
from app.features.calorias.calculo_calorias_diarias import calcular_gasto_calorico_diario
from app.features.imc.calculo_imc import calcular_imc

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/nutrition', methods=['GET', 'POST'])
def nutrition():
    imc_data = None  # Variável para armazenar o resultado do IMC
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])/100

        # Calcula o IMC com base no peso e altura
        imc_data = calcular_imc(altura, peso)

    # Renderiza a página com o resultado do IMC (se houver)
    return render_template('nutrition.html', imc_result=imc_data)

@main_bp.route('/calories', methods=['GET', 'POST'])
def calories():
    resultado = None  # Variável para armazenar o resultado do gasto calórico
    if request.method == 'POST':
        # Captura os dados enviados pelo formulário
        sexo = request.form['sexo']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        idade = int(request.form['idade'])
        nivel_atividade = request.form['nivel_atividade']

        # Calcula o gasto calórico diário
        resultado = calcular_gasto_calorico_diario(sexo, peso, altura, idade, nivel_atividade)

    # Renderiza a página com o resultado do gasto calórico (se houver)
    return render_template('calories.html', resultado=resultado)

@main_bp.route('/water')
def water():
    return render_template('water.html')