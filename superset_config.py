import os

# Database configuration - SQLite simple
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Security
SECRET_KEY = 'superset-secret-key-2024-production-deployment-railway-secure'

# Configuration minimale pour éviter les erreurs
FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": False,
    "DASHBOARD_NATIVE_FILTERS": False,
    "DASHBOARD_CROSS_FILTERS": False,
    "DASHBOARD_NATIVE_FILTERS_SET": False,
    "GLOBAL_ASYNC_QUERIES": False,
    "EMBEDDED_SUPERSET": False,
}

# Désactiver les fonctionnalités problématiques
WTF_CSRF_ENABLED = False
WTF_CSRF_TIME_LIMIT = None

# Configuration simple
PUBLIC_ROLE_LIKE_GAMMA = True

# Cache simple
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# Logging
LOG_LEVEL = 'INFO'
