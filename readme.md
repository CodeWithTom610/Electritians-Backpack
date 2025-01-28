# EBT-Backpack

EBT-Backpack ist eine Webanwendung, die verschiedene Tools und Funktionen bietet, um den Benutzern zu helfen, ihre Aufgaben effizient zu erledigen. Die Anwendung nutzt Flask als Web-Framework und bietet eine Vielzahl von Funktionen, darunter Benutzerverwaltung, Nachrichtenverwaltung und verschiedene Berechnungstools.

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Funktionen](#funktionen)
- [Beitrag](#beitrag)
- [Lizenz](#lizenz)

## Installation

1. Klone das Repository:
    ```sh
    git clone https://github.com/dein-benutzername/ebt-backpack.git
    ```
2. Wechsle in das Projektverzeichnis:
    ```sh
    cd ebt-backpack
    ```
3. Erstelle und aktiviere eine virtuelle Umgebung:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Auf Windows: venv\Scripts\activate
    ```
4. Installiere die Abhängigkeiten:
    ```sh
    pip install -r requirements.txt
    ```
5. Erstelle die Datenbank:
    ```sh
    flask db upgrade
    ```

## Verwendung

1. Starte die Anwendung:
    ```sh
    flask run
    ```
2. Öffne deinen Webbrowser und gehe zu `http://127.0.0.1:5000`.

## Funktionen

- **Benutzerverwaltung**: Erstelle, bearbeite und lösche Benutzer.
- **Nachrichtenverwaltung**: Verwalte Nachrichtenartikel.
- **Berechnungstools**: Verschiedene Tools zur Berechnung von Widerständen und anderen Werten.
- **Wissensdatenbank**: Füge Einträge zur Wissensdatenbank hinzu und verwalte sie.

## Beitrag

Beiträge sind willkommen! Bitte erstelle einen Fork des Repositories und sende einen Pull-Request mit deinen Änderungen.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.