"""
QATRA – Application Entry Point
Run with: python run.py  (dev)
Deployed via: gunicorn run:app
"""
import os
from app import create_app

env = os.environ.get("FLASK_ENV", "production")
app = create_app(env)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        debug=(env == "development"),
    )
