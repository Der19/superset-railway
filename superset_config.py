import os

# Database configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security - SECRET_KEY simple
SECRET_KEY = 'superset-simple-key-2024'

# DÉSACTIVER COMPLÈTEMENT L'AUTHENTIFICATION
AUTH_TYPE = 0  # AUTH_NONE - Pas d'authentification
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = "Public"

# Configuration Superset
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "DASHBOARD_NATIVE_FILTERS": True,
    "DASHBOARD_CROSS_FILTERS": True,
    "DASHBOARD_NATIVE_FILTERS_SET": True,
    "GLOBAL_ASYNC_QUERIES": False,
    "EMBEDDED_SUPERSET": True,
}

# DÉSACTIVER toutes les sécurités
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None
SECURITY_PASSWORD_SALT = None
SECURITY_PASSWORD_HASH = None

# Accès public total
PUBLIC_ROLE_LIKE_GAMMA = True

# Cache simple
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging
LOG_LEVEL = 'INFO'

# Désactiver les middlewares de sécurité
ENABLE_CORS = False
RATELIMIT_ENABLED = False
