# Importiere die notwendige Funktion und das Datenbankobjekt aus der app
from app import create_app
from app import db

# Erstelle die Flask-App durch Aufruf der Funktion create_app()
app = create_app()

# Stelle sicher, dass die Datenbanktabellen existieren.
# Dies wird im Kontext der Anwendung durchgeführt (daher app.app_context()).
# Die Funktion db.create_all() erstellt alle Tabellen, die in den Modellen definiert sind, falls diese noch nicht existieren.
with app.app_context():
    db.create_all()

# Überprüfe, ob dieses Skript als Hauptmodul ausgeführt wird.
# Wenn ja, starte den Flask-Server.
if __name__ == '__main__':
    # Starte den Server auf localhost (127.0.0.1) und Port 8000.
    # Der Debug-Modus ist aktiviert, damit Änderungen sofort übernommen werden und Fehler detailliert angezeigt werden.
    app.run(host='127.0.0.1', port=8000, debug=True)
