from app import  create_app
from create_db_app import app

# app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
