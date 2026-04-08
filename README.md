# 💧 QATRA – Gestion Intelligente de l'Eau

QATRA est une application web Flask permettant de suivre, simuler et analyser
la consommation d'eau domestique, pièce par pièce, avec des graphiques en temps
réel, un système de gamification XP/rang, et un assistant chatbot.

---

## 🚀 Démarrage rapide

```bash
# 1. Cloner / décompresser le projet
cd qatra_improved

# 2. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python run.py
```

Ouvrir **http://localhost:8000** dans votre navigateur.

> **Compte de démonstration** : `demo` / `demo1234`

---

## 📁 Structure du projet

```
qatra_improved/
├── run.py                      ← Point d'entrée
├── config.py                   ← Configuration multi-environnements
├── requirements.txt
├── app/
│   ├── __init__.py             ← Application Factory + seeder
│   ├── models/
│   │   ├── user.py             ← Utilisateur (auth, XP, rang)
│   │   ├── maison.py           ← Maison virtuelle
│   │   ├── piece.py            ← Pièces de la maison
│   │   └── consommation.py     ← Enregistrements de consommation
│   ├── forms/
│   │   └── auth_forms.py       ← Formulaires WTForms validés
│   ├── routes/
│   │   ├── main.py             ← Pages principales (Blueprint)
│   │   └── auth.py             ← Authentification (Blueprint)
│   ├── api/
│   │   └── consumption.py      ← API REST JSON
│   └── utils/
│       └── helpers.py          ← Fonctions utilitaires
├── templates/
│   ├── base.html               ← Template de base (flash messages)
│   ├── welcome.html            ← Page d'accueil
│   ├── login.html              ← Connexion
│   ├── register.html           ← Inscription
│   ├── dashboard.html          ← Tableau de bord
│   ├── maison.html             ← Maison virtuelle interactive
│   └── application.html        ← Application analytique complète
└── static/
    └── images/logo.png
```

---

## 🔌 API REST

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/api/user` | Infos utilisateur (XP, rang, limite) |
| POST | `/api/user/limit` | Mettre à jour la limite mensuelle |
| GET | `/api/consumption/today` | Total du jour en litres |
| GET | `/api/consumption/rooms` | Consommation par pièce (aujourd'hui) |
| GET | `/api/consumption/history?days=30` | Historique quotidien agrégé |
| POST | `/api/consumption/log` | Enregistrer une consommation |

---

## 🏗️ Architecture

- **Application Factory** (`create_app()`) — testable, extensible
- **Blueprints** — séparation claire des responsabilités
- **SQLAlchemy ORM** — requêtes agrégées optimisées, index composite
- **Flask-Login** — sessions sécurisées, `@login_required`
- **Flask-WTF + CSRF** — protection contre les attaques CSRF
- **Werkzeug** — hachage des mots de passe (PBKDF2-SHA256)

---

## ✨ Fonctionnalités

- 🔐 Inscription / connexion sécurisées
- 🏠 Maison virtuelle interactive avec simulation de consommation
- 📊 Graphiques en temps réel (Chart.js) : historique + répartition par pièce
- 🏅 Gamification : XP + rangs (Bronze → Argent → Or → Platine)
- 💡 Conseils quotidiens rotatifs basés sur la date
- 🤖 Chatbot assistant intégré (glissable)
- 🔔 Messages flash avec auto-dismiss
- 📱 Responsive design

---

## ⚙️ Variables d'environnement

| Variable | Défaut | Description |
|----------|--------|-------------|
| `SECRET_KEY` | valeur de dev | Clé secrète Flask (changer en prod !) |
| `DATABASE_URL` | SQLite local | URL de connexion base de données |
| `FLASK_ENV` | `development` | Environnement (`development`/`production`) |
| `PORT` | `8000` | Port d'écoute |
