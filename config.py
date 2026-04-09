"""
QATRA – Configuration Module
"""
import os
from datetime import timedelta


class Config:
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "qatra-dev-secret-change-in-production")
    WTF_CSRF_ENABLED: bool = True

    BASE_DIR: str = os.path.abspath(os.path.dirname(__file__))
    # Fix: handle postgres:// → postgresql:// (Render uses the old scheme)
    _db_url = os.environ.get("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'qatra.db')}")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI: str = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    PERMANENT_SESSION_LIFETIME: timedelta = timedelta(days=7)
    DEFAULT_MONTHLY_LIMIT: int = 3_000
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


config_map: dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
