# Data parser és Inserter 5000 ultramega kígyó XXL

Az alábbi app egy python alapú parser ami különböző kiterjesztésű file-okat lefordítja SQL query-re és betölti egy Postgres adatbázisba.  

# Támogatott kiterjesztészek:

* .xlsx
* .csv
* .json
* .txt

# Elvárt folyamat:

- Felhasználó belép és autentikál a webfelületre
- Létrehozza az adatbáziskapcsolatot 
- A kezelőfelületen pedig kiválasztja e betöltendő file-t és elindítja a folyamatot

# Tech stack:

- Python
- HTML/CSS
- Postrgres

# Dependencies:

- Python 3.13.12
- Flaskcharset-normalizer 3.4.7
- click              8.3.2
- colorama           0.4.6
- Flask              3.1.3
- idna               3.11
- itsdangerous       2.2.0
- Jinja2             3.1.6
- MarkupSafe         3.0.3
- numpy              2.4.4
- pandas             3.0.2
- pip                25.3
- psycopg2           2.9.11
- python-dateutil    2.9.0.post0
- requests           2.33.1
- six                1.17.0
- tzdata             2026.1
- urllib3            2.6.3
- Werkzeug           3.1.8