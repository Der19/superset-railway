import os

# Database configuration - SQLite en mémoire
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security - SECRET_KEY simple
SECRET_KEY = 'superset-simple-key-2024'

# Configuration Superset SANS sécurité
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": False,
    "EMBEDDED_SUPERSET": True,
}

# DÉSACTIVER toutes les mesures de sécurité
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None
SECURITY_PASSWORD_SALT = None
SECURITY_PASSWORD_HASH = None

# Accès public total
PUBLIC_ROLE_LIKE_GAMMA = True
AUTH_TYPE = 0  # AUTH_NONE - Pas d'authentification
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

# Cache simple
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging simple
LOG_LEVEL = 'INFO'

# Désactiver CORS et autres sécurités
ENABLE_CORS = False
RATELIMIT_ENABLED = False
