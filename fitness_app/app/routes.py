from flask import Blueprint, render_template

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

@main_bp.route('/calories')
def calories():
    return render_template('calories.html')
