# ⚽ Football Odds Dashboard (Serie A)

Progetto Python che mostra le quote in tempo reale delle partite di Serie A, utilizzando dati aggiornati da API esterne.

Le quote vengono recuperate da The Odds API e visualizzate in una dashboard web semplice e intuitiva.

---

# 🚀 Come funziona

Il progetto è composto da due parti:

## 🧠 Backend (Python)
- Recupera le partite di Serie A
- Filtra la prossima giornata
- Estrae le quote 1X2
- Salva i dati in `odds.json`

## 🌐 Frontend (HTML + JS)
- Legge il file `odds.json`
- Mostra le partite in una dashboard grafica
- Permette il refresh dei dati

---

# 📁 Struttura del progetto

football-odds-dashboard/
│
├── main.py        # backend Python (API fetch)
├── odds.json      # dati generati automaticamente
├── index.html     # dashboard grafica
├── README.md

---

# ▶️ Come farlo partire

## 1. Generare le quote (backend Python)

Esegui nella cartella del progetto:

python main.py

Questo:
- si collega a The Odds API
- prende la prossima giornata di Serie A
- crea/aggiorna il file odds.json

---

## 2. Avviare la dashboard

Esegui:

python -m http.server 8000

Poi apri nel browser:

http://localhost:8000

---

## 3. Aggiornare i dati

Ogni volta che vuoi nuove quote:

python main.py

Poi ricarica la pagina del browser.

---

# 📊 Cosa mostra

Per ogni partita:

- ⚽ Squadra casa vs squadra trasferta  
- 📈 Quote 1X2:
  - 1 = vittoria casa
  - X = pareggio
  - 2 = vittoria trasferta

---

# ⚠️ Note

- Le quote sono fornite da API esterne e possono cambiare nel tempo
- Non tutti i bookmaker sono sempre disponibili
- Il progetto è a scopo educativo e portfolio


# 🧠 Tecnologie usate

- Python
- HTML / CSS / JavaScript
- API esterne (The Odds API)
