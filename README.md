# QATRA 💧 — Water Consumption Tracker

A Flask web application for tracking household water usage, gamification, and conservation goals.

## Demo credentials
- **Username:** `demo` | **Password:** `demo1234`

## Local setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # edit SECRET_KEY
FLASK_ENV=development python run.py
```
Visit http://localhost:8000

## Deploy to Render
1. Push to GitHub
2. New → Web Service → connect repo
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn run:app --bind 0.0.0.0:$PORT --workers 2`
5. Add env var: `SECRET_KEY` = (generate a random string)

## Project structure
```
qatra/
├── app/
│   ├── api/          # REST JSON endpoints
│   ├── forms/        # WTForms definitions
│   ├── models/       # SQLAlchemy models
│   ├── routes/       # HTML page routes
│   └── utils/        # Helper functions
├── templates/        # Jinja2 HTML templates
├── static/           # CSS / JS / images
├── config.py         # Environment configurations
├── run.py            # Entry point
├── Procfile          # Render/Heroku process file
└── requirements.txt
```
