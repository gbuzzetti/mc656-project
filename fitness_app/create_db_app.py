from app import create_app, db

#NÃO RODAR NOVEMENTE, O BANCO DE DADOS JÁ FOI CRIADO

app = create_app()

with app.app_context():  # Ensures application context is active
    db.create_all()       # Creates the tables
    print("Database tables created successfully.")
