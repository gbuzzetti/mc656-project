from flask import Blueprint, render_template, request
from app.features.calorias.calculo_calorias_diarias import calcular_gasto_calorico_diario

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@main_bp.route('/water')
def water():
    return render_template('water.html')

@main_bp.route('/calories', methods=['GET', 'POST'])
def calories():
    if request.method == 'POST':
        sexo = request.form['sexo']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        idade = int(request.form['idade'])
        nivel_atividade = request.form['nivel_atividade']

        resultado = calcular_gasto_calorico_diario(sexo, peso, altura, idade, nivel_atividade)
        return render_template('calories.html', resultado=resultado)
    return render_template('calories.html')