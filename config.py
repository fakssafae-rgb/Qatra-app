"""
QATRA – Configuration Module
Centralizes all application settings using environment variables with sensible defaults.
"""

import os
from datetime import timedelta


class Config:
    """Base configuration shared across all environments."""

    # ── Security ──────────────────────────────────────────────────────────────
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "qatra-dev-secret-change-in-production")
    WTF_CSRF_ENABLED: bool = True

    # ── Database ──────────────────────────────────────────────────────────────
    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        "DATABASE_URL",
        f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'qatra.db')}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # ── Session ───────────────────────────────────────────────────────────────
    PERMANENT_SESSION_LIFETIME: timedelta = timedelta(days=7)

    # ── Water limits (litres/month defaults) ──────────────────────────────────
    DEFAULT_MONTHLY_LIMIT: int = 3_000  # litres

    # ── Pagination ────────────────────────────────────────────────────────────
    RECORDS_PER_PAGE: int = 20


class DevelopmentConfig(Config):
    DEBUG: bool = True
    TESTING: bool = False


class ProductionConfig(Config):
    DEBUG: bool = False
    TESTING: bool = False
    WTF_CSRF_ENABLED: bool = True


class TestingConfig(Config):
    TESTING: bool = True
    WTF_CSRF_ENABLED: bool = False
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"


# ── Registry ──────────────────────────────────────────────────────────────────
config_map: dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
