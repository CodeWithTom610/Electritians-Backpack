from app import create_app
from app import db

app = create_app()

# Erstellen der Datenbanktabellen, falls diese noch nicht existieren
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
