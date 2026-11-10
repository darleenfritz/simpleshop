# Simple Shop

Ein REST-Backend für einen kleinen Onlineshop, entwickelt mit Django und dem Django REST Framework. Es verwaltet Kunden, Adressen, Produkte und Warenkörbe, schützt Schnittstellen über JWT-Anmeldung und dokumentiert alle Endpunkte automatisch mit Swagger. Eine kleine HTML- und JavaScript-Oberfläche zeigt, wie ein Frontend die Schnittstelle abfragt.

## Hintergrund

Simple Shop entstand als Einzelarbeit im Modul „Web-Programmierung 3“ im Studiengang E-Commerce an der Technischen Hochschule Würzburg-Schweinfurt (THWS), Wintersemester 2024/25.

**Hinweis:** Das Projekt ist eine Übungsanwendung zum Lernen von Django und REST-Schnittstellen. Es ist für den Betrieb auf dem eigenen Rechner gedacht und nicht für den echten Einsatz eingerichtet, zum Beispiel ist der Debug-Modus aktiv und CORS für alle Herkünfte freigegeben.

## Funktionen

- **Kunden:** Anlegen, Abrufen, Ändern und Löschen; jeder Kunde ist mit einem Django-Benutzerkonto verknüpft
- **Adressen:** Mehrere Adressen pro Kunde
- **Produkte:** Name, Produktnummer, Netto- und Bruttopreis
- **Warenkorb:** Ein Warenkorb pro Kunde mit Positionen, Netto- und Bruttosummen sowie Steueranteil; Produkte hinzufügen nur für angemeldete Benutzer
- **Anmeldung:** Registrierung und Login über Djoser, Zugriff mit JWT-Token
- **API-Dokumentation:** Swagger-Oberfläche mit allen Endpunkten
- **Admin-Bereich:** Angepasste Django-Admin-Ansicht für Kunden, unter anderem mit Anzeige der Passwortstärke
- **Kundenübersicht:** Kleine Weboberfläche (`JS and HTML File/crm.html`), die einen Kunden über seine Nummer sucht und seine Adressen als Tabelle anzeigt

## Schnittstellen

| Pfad | Methoden | Inhalt |
| --- | --- | --- |
| `/customer/` | GET | Alle Kunden |
| `/customer/customers` | GET, POST | Kunden abrufen und anlegen |
| `/customer/<id>` | GET, PUT, DELETE | Einzelner Kunde |
| `/addresses/` | GET, POST | Alle Adressen |
| `/addresses/<id>` | GET, PUT, DELETE | Einzelne Adresse |
| `/products/` | GET, POST | Alle Produkte |
| `/products/<id>` | GET, PUT, DELETE | Einzelnes Produkt |
| `/cart/` | GET, POST | Alle Warenkörbe |
| `/cart/<id>` | GET, PUT, DELETE | Einzelner Warenkorb |
| `/cart/perform/add-to-cart` | POST | Produkt in den Warenkorb legen (nur angemeldet) |
| `/auth/` | | Registrierung und JWT-Login über Djoser |
| `/api/swagger` | GET | API-Dokumentation |
| `/admin/` | | Django-Admin |

## Technik

| Bereich | Umsetzung |
| --- | --- |
| Sprache | Python 3.12 |
| Framework | Django 5.1, Django REST Framework |
| Anmeldung | Djoser, Simple JWT |
| Dokumentation | drf-yasg (Swagger) |
| Datenbank | SQLite |
| Frontend | HTML, JavaScript, Bootstrap 4 |

Das Projekt ist in vier Django-Apps aufgeteilt: `customermanager`, `addressmanager`, `productmanager` und `cartmanager`. Jede App hat eigene Modelle, Serializer, Views und URLs.

## Lokal starten

1. Repository klonen und eine virtuelle Umgebung anlegen:
   ```
   git clone https://github.com/darleenfritz/simpleshop.git
   cd simpleshop
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Pakete installieren:
   ```
   pip install -r requirements.txt
   ```
3. Datei `.env.example` nach `.env` kopieren und einen geheimen Schlüssel eintragen:
   ```
   cp .env.example .env
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Den ausgegebenen Schlüssel hinter `DJANGO_SECRET_KEY=` in die `.env` einfügen.
4. Datenbank anlegen, Admin-Konto erstellen und Server starten:
   ```
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
5. Die Swagger-Dokumentation ist danach unter `http://127.0.0.1:8000/api/swagger` erreichbar, die Kundenübersicht öffnet man direkt als Datei `JS and HTML File/crm.html` im Browser.

## Autorin

Darleen Fritz, Studentin E-Commerce an der THWS
