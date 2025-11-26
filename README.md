# 2IT Server Admin Panel

Dette prosjektet er et serverbasert admin-panel utviklet som prosjektoppgave i
Informasjonsteknologi Vg2.  
Løsningen er bygget med **Flask**, **MariaDB/MySQL** og fokus på **sikkerhet, struktur og forståelse**.

Prosjektet inneholder både backend, database og et enkelt webgrensesnitt for innlogging og administrasjon.

---

## Funksjoner

- Innlogging og registrering av brukere
- Admin- og brukerroller
- Sikker lagring av passord (hashing)
- Dashboard-side for innloggede brukere
- Logout-funksjon
- Databasekobling med miljøvariabler (.env)

---

## Sikkerhet

Prosjektet er laget med fokus på sikkerhet:

- Passord lagres **aldri i klartekst**
- Passord hashes før lagring i database
- Sensitive verdier lagres i `.env`-fil
- `.env` er ekskludert fra GitHub med `.gitignore`
- Kun innloggede brukere har tilgang til dashboard

---

##  Teknologi brukt

- **Python (Flask)**
- **MariaDB / MySQL**
- **HTML / CSS**
- **GitHub (versjonskontroll og prosjektplanlegging)**

---

##  Database

Databasen inneholder blant annet:
- Brukere
- Administratorer
- Roller (admin / user)

Databaseforbindelsen håndteres i `db.py` og bruker miljøvariabler for sikker tilgang.

---

## Hvordan kjøre prosjektet lokalt

1. Klon repository:
   ```bash
   git clone https://github.com/Pramis01/Server-Admin-Panel
2. Installer avhengigheter:
    ```bash
    pip install -r requirements.txt
3. Lag en .env-fil med:
     ```bash
    DB_HOST=
    DB_USER=
    DB_PASSWORD=
    DB_NAME=
    SECRET_KEY=
4. Opprett admin-bruker:
    ```bash
    python create_admin.py
5. Start Flask-applikasjonen:
    ```bash
    python app.py
##  Brukerveiledning

1. Gå til innloggingssiden og logg inn med brukernavn og passord
2. Etter innlogging vises dashboard
3. Dashboard viser informasjon om innlogget bruker
4. Bruk Logout for å logge ut
5. Kun innloggede brukere har tilgang til dashboard

##  Registrering brukerveiledning

1. Gå til registreringssiden
2. Fyll inn brukernavn og passord
3. Velg rolle (admin eller bruker)
4. Trykk Registrer
5. Brukeren lagres i databasen
6. Du kan deretter logge inn med den nye kontoen

## Prosjektplanlegging

Prosjektet er planlagt og dokumentert ved bruk av GitHub Projects (Kanban).
Arbeidet er delt inn i:

- Backlog

- To Do

- In Progress

- Testing

- Done

Dette gir oversikt over fremdrift og struktur i prosjektet.

## Formål

Formålet med prosjektet er å vise kompetanse innen:

- Programmering

- Databaser

- Sikkerhet og personvern

- Drift og infrastruktur

- Dokumentasjon og planlegging