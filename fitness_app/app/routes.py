from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app import LoginForm, RegisterForm, bcrypt, db, User
from flask_login import login_required, login_user, logout_user, current_user
from app.features.facade import Facade

main_bp = Blueprint('main', __name__)
facade = Facade()

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
        imc_data = facade.calcular_imc(altura, peso)

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
        resultado = facade.calcular_gasto_calorico_diario(sexo, peso, altura, idade, nivel_atividade)

    # Renderiza a página com o resultado do gasto calórico (se houver)
    return render_template('calories.html', resultado=resultado)

@main_bp.route('/water', methods=['GET', 'POST'])
def water():
    water_result = None  # Variável para armazenar o resultado da quantidade de água
    if request.method == 'POST':
        try:
            # Captura os dados enviados pelo formulário
            kg = float(request.form['peso'])

            # Cálculo da quantidade de água
            water_result = facade.calcular_recomendacao_agua(kg)
        except (ValueError, KeyError):
            water_result = 'Erro ao processar os dados. Verifique os valores inseridos.'

    # Renderiza a página com o resultado da quantidade de água (se houver)
    return render_template('water.html', resultado=water_result)

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))

    return render_template('login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@main_bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))